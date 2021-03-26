#define RELE 8
#define LEDR_PIN 11
#define LEDB_PIN 10
#define LEDG_PIN 9
#define ATIVA_LEDR "2"
#define DEACTIVATE_LEDR "3"
#define ACTIVATE_LEDG "4"
#define DEACTIVATE_LEDG "5"
#define ACTIVATE_LEDB "6"
#define DEACTIVATE_LEDB "7"
#define TEMP "8"
#define LUZ "9"
#define ACTIVATE_RELE "A"
#define DEACTIVATE_RELE "B"

const int LM35 = A0;
float temperatura = 0;
int ADClido = 0;

const int LDR = A1;
int candela = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(LEDR_PIN, OUTPUT);
  pinMode(LEDG_PIN, OUTPUT);
  pinMode(LEDB_PIN, OUTPUT);
  pinMode(RELE, OUTPUT);
  analogReference(INTERNAL);
}

void loop() 
{
  String s = Serial.readString();

  if(s == ATIVA_LEDR)
  {
    digitalWrite(LEDR_PIN, HIGH);
    Serial.println("RED LED ON");
  }
  else
  if(s == DEACTIVATE_LEDR)
  {
    digitalWrite(LEDR_PIN, LOW);
    Serial.println("RED LED OFF");
  }
  else
  if(s == ACTIVATE_LEDG)
  {
    digitalWrite(LEDG_PIN, HIGH);
    Serial.println("GREEN LED ON");
  }
  else
  if(s == DEACTIVATE_LEDG)
  {
    digitalWrite(LEDG_PIN, LOW);
    Serial.println("GREEN LED OFF");
  }
  else
  if(s == ACTIVATE_LEDB)
  {
    digitalWrite(LEDB_PIN, HIGH);
    Serial.println("BLUE LED ON");
  }
  else 
  if(s == DEACTIVATE_LEDB)
  {
    digitalWrite(LEDB_PIN, LOW);
    Serial.println("BLUE LED OFF");
  }
  else
  if(s == ACTIVATE_RELE)
  {
    digitalWrite(RELE, HIGH);
    Serial.println("RELE ON");
  }
  else 
  if(s == DEACTIVATE_RELE)
  {
    digitalWrite(RELE, LOW);
    Serial.println("RELE OFF");
  }
  else 
  if(s == TEMP)
  {
    ADClido = analogRead(LM35);
    temperatura = ADClido * 0.1455;
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" Cº");
  }
  else
  if(s == LUZ)
  {
    candela = analogRead(LDR);
    Serial.print("LDR: ");
    Serial.print(candela);
    Serial.println("cd");
  }
}