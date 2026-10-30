<?php
// Receives the request form from index.html#kontakt and forwards it by e-mail to the practice.
// Answers JSON for the page script; without JavaScript it redirects back with ?anfrage=ok|fehler.

const TO   = 'christoph.manicke@gmx.de';
const FROM = 'anfrage@example.de'; // TODO: an address on the site's own domain, so the hoster's mail server may send it

const TOPICS = [
  'Zweitmeinung vor einer Operation',
  'Beschwerden nach einer Operation',
  'Beratung bei Rückenbeschwerden',
  'Andere neurochirurgische Frage',
];
const TIMES = [
  'So bald wie möglich',
  'In den nächsten zwei Wochen',
  'Im nächsten Monat',
  'Ich bin flexibel',
];

date_default_timezone_set('Europe/Berlin');

$wantsJson = str_contains($_SERVER['HTTP_ACCEPT'] ?? '', 'application/json');

function answer(bool $ok, int $status, string $error = ''): never {
  global $wantsJson;
  http_response_code($status);
  if ($wantsJson) {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($ok ? ['ok' => true] : ['ok' => false, 'error' => $error], JSON_UNESCAPED_UNICODE);
  } else {
    header('Location: index.html?anfrage=' . ($ok ? 'ok' : 'fehler') . '#kontakt', true, 303);
  }
  exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') answer(false, 405, 'Nur POST.');

// Bots fill the hidden field; people never see it.
if (trim($_POST['website'] ?? '') !== '') answer(true, 200);

// One-line fields must not carry line breaks into the mail headers.
$line = fn (string $key, int $max) => mb_substr(trim(preg_replace('/[\r\n\t]+/', ' ', (string) ($_POST[$key] ?? ''))), 0, $max);

$name  = $line('name', 120);
$email = $line('email', 200);
$topic = $line('anliegen', 80);
$time  = $line('zeitraum', 80);
$note  = mb_substr(trim((string) ($_POST['nachricht'] ?? '')), 0, 2000);
$consent = ($_POST['einwilligung'] ?? '') !== '';

if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || !$consent) {
  answer(false, 422, 'Bitte Name, eine gültige E-Mail-Adresse und die Einwilligung angeben.');
}
if (!in_array($topic, TOPICS, true)) $topic = 'Nicht angegeben';
if (!in_array($time, TIMES, true)) $time = 'Nicht angegeben';

$body = "Neue Anfrage über die Website\n\n"
  . "Name: $name\n"
  . "E-Mail: $email\n"
  . "Anliegen: $topic\n"
  . "Zeitraum: $time\n\n"
  . ($note !== '' ? "Nachricht:\n$note\n\n" : '')
  . "Einwilligung zur Verarbeitung erteilt am " . date('d.m.Y, H:i') . " Uhr.\n";

$headers = [
  'From' => 'Website Dr. Manicke <' . FROM . '>',
  'Reply-To' => $email,
  'Content-Type' => 'text/plain; charset=UTF-8',
  'Content-Transfer-Encoding' => '8bit',
  'MIME-Version' => '1.0',
];
$subject = '=?UTF-8?B?' . base64_encode("Anfrage: $topic") . '?=';

$sent = @mail(TO, $subject, $body, $headers, '-f' . FROM);
$sent ? answer(true, 200) : answer(false, 502, 'Die Anfrage konnte nicht gesendet werden.');
