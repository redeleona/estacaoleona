/*===========================
 Arduino:Serial Pan-Tilt Protocol by Livia Miura 
 ============================*/
char string[25];
int i=0;
int string_len, num, inByte, c;
char aux;
int a, b;
float x;

const int pinReset =7;
const int pin2 = 8;    // LED conectado ao pino digital 2 
const int pin3 = 9;   //3
const int pin4 = 10;  //4
const int pin5 = 11;  //5
const int pin6 = 12;  //6
const int pin7 = 13;  //7

void setup() {

  Serial.begin(9600);      // Define a taxa de dados em bits por segundo(baud)para transmissão de dados. 

  pinMode(pin2,OUTPUT);    // Configura o pino especificado se comportar tanto como uma entrada ou uma saída.
  pinMode(pin3,OUTPUT);    // Define o pino digital como saída. 
  pinMode(pin4,OUTPUT);
  pinMode(pin5,OUTPUT);
  pinMode(pin6,OUTPUT);
  pinMode(pin7,OUTPUT);
}
void loop() // LOOP FUNCTION
{
  inByte = Serial.read();
  string_len=0;                      // Incremento recebe 0.
  if (inByte == '!')
    read_serial();  // If Start of line ("!") é encontrada, chama a função read_serial().
  delay(100);                        // Fundamental para o funcionamento do "!"   

}



void read_serial()                   // função que irá receber graus e o comando
{
  
  Serial.print(" Inicio Leitura\n"); 

  while (inByte!='*') // As long as EOL "End of Line" não for encontrado, mantém a leitura

    if (Serial.available() > 0) // if new data is available
    {
      inByte = Serial.read(); // Read new byte
      string[string_len] = inByte; // Save the data in a character array
      Serial.print("String lida:");
      Serial.println(string[string_len]); // Print the characters that was recieved
      string_len++;
       Serial.print("You sent me:");
   // Serial.write(inByte);
      Serial.println("---------------------");
    }

    else if (Serial.available() == 0)
    {
      Serial.println("End of Line não disponivel, dados inválidos");  
      break;
    }

  if (inByte == '*')
  {

    for (i=0;i<(string_len-1);i++)
    {
      // Serial.println(string[i]);
      num = atoi(string);       //atoi () converte uma matriz de caracteres ASCII para um inteiro
    }

    Serial.print("Graus: ");
    Serial.println(num);
 // Serial.write(num);//java
  Serial.print("You sent me dentro:");
 // Serial.write(inByte);
 
   Serial.println("---------------------");
   Serial.print("You number:");
   x=28;
   int d = x+7;

  Serial.println(d);
   Serial.write(d);
   Serial.println("---------------------");
  

    Serial.print("Comando:");
    aux= string[3];   // recebe o comando L,R,U,D,S,O ou F
    Serial.println(aux);
  }// Fim do if

  switch(aux){

  case 'L'://Left
    setAzimuth(num,1);
    num=0;
    break;

  case 'R'://Right
    setAzimuth(num,0);
    num=0;
    break;

  case 'U':  //UP
    setElevation(num,1);
    break;

  case 'D': // Down
    setElevation(num,0);
    break;

  case 'O': // camera ON
    turnCameras(1);
    break;

  case 'F': // camera OFF
    turnCameras(0);
    break;

  case 'S': // reset Pantilt
    resetPantilt();
    break;

  case 'A':
    acenderLed();
    break;    
    
  case 'B':
    apagarLed();
    break;
  }// fim do switch*/
}//fim read_serial

void acenderLed()
{
  digitalWrite(pin2,HIGH);
  Serial.println( "Acendeu LED");
}

void apagarLed()
{
  digitalWrite(pin2,LOW);
  Serial.println( "Apagou LED");
}

void resetPantilt()
{
  Serial.println( "Entrei no resetPT");


  digitalWrite(pin4,HIGH); // define o LED on
  delay(2120);  // aguarda 43 segundos 
  digitalWrite(pin4,LOW); // define o LED off 

  //Reset the elevation to 0
  digitalWrite(pin3,HIGH);
  delay(4300);  
  digitalWrite(pin3,LOW);
  delay(200);

  /* o que era antes da  modificação do pinos up and down
   digitalWrite(pin4,HIGH); // define o LED on
   delay(4300);           // aguarda 43 segundos 
   digitalWrite(pin4,LOW); // define o LED off 
   delay(200);
   digitalWrite(pin3,HIGH);
   delay(2120);
   digitalWrite(pin3,LOW);
   */


  //Reset the Azimuth
  digitalWrite(pin5,HIGH);
    digitalWrite(pin7,HIGH);
  delay(7000);
  digitalWrite(pin5,LOW);
  digitalWrite(pin7,LOW);
  delay(500);
}



void turnCameras(int command)
{
  if (command == 1)
  {
    digitalWrite(pin2,HIGH);
  }
  else if (command == 0)
  {
    digitalWrite(pin2,LOW);
       
  }
}

//elevação do tilt direção


void setElevation(int numbe,int dir)
{
  if (dir == 1) //cima  foi alterado os pinos dia 31/07/14  trocou no cabo do pantilt.
  {
    digitalWrite(pin4,HIGH);
     digitalWrite(pin7,HIGH);
    //Serial.println(numbe);
    float nu = (numbe / 2.19)*1000;
    //Serial.println(long(nu)*1000);
    delay(long(nu));
    digitalWrite(pin4,LOW);
       digitalWrite(pin7,LOW);
    delay(200);
    nu = 0;
  }
  else if (dir == 0) // baixo
  {
    digitalWrite(pin3,HIGH);
      digitalWrite(pin7,HIGH);
    //Serial.println(numbe);
    float nu = (numbe / 2.26)*1000;
    //Serial.println(long(nu));
    delay(long(nu));
    digitalWrite(pin3,LOW);
       digitalWrite(pin7,LOW);
    delay(500);
    nu = 0;
  }
}

//direção pan esquerda e direita

void setAzimuth(int numbe,int dir)
{
  if (dir == 1) // esquerda 
  {

    digitalWrite(pin5,HIGH);
      digitalWrite(pin7,HIGH);
    //Serial.println(numbe);
    float nu = (numbe / 10.9375)*1000;
    //Serial.println(long(nu)*1000);
    delay(long(nu));
    digitalWrite(pin5,LOW);
       digitalWrite(pin7,LOW);
    delay(500);
    nu = 0;
    numbe=0; //reset



  }
  else if (dir == 0)  // direita
  {
    digitalWrite(pin6,HIGH);
      digitalWrite(pin7,HIGH);
    //Serial.println(numbe);
    float nu = (numbe / 10.9375)*1000;
    //Serial.println(long(nu));
    delay(long(nu));
    digitalWrite(pin6,LOW);
       digitalWrite(pin7,LOW);
    delay(500);
    nu = 0;
    numbe=0; //reset
    //  string_len =0;//reset
  }
}






































