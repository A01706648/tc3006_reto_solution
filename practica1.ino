//Sensor de temperatura usando el LM35 o TMP36 junto con un LCD
//Definiciones
int pin_sensor = A0; // Define el pin analogico del LM35
int valorA0;         //Variable entera para leer el valor de A0

 
void setup() {
 Serial.begin(9600);   // Inicia la comunicación con el monitor serial de Arduino
} 
 
//Función que será ejecutada continuamente
void loop() {
  //Lectura del Pin A0 (ADC)
  valorA0=analogRead(pin_sensor); // Almacena el valor entero.
  Serial.println(valorA0); 
  delay(1000); //Imprime el valor cada segundo
}
