#include <Wire.h>

//Direccion I2C de la IMU
#define MPU 0x68
#define MPU2 0x69
//Ratios de conversion
#define A_R 16384.0
#define G_R 131.0

//Conversion de radianes a grados 180/PI
#define RAD_A_DEG = 57.295779

//MPU-6050 da los valores en enteros de 16 bits
//Valores sin refinar
int16_t AcX, AcY, AcZ, GyX, GyY, GyZ;
int16_t AcX2, AcY2, AcZ2, GyX2, GyY2, GyZ2;
//Angulos
float Acc[2];
float Gy[2];
float Angle[2];
float Acc2[2];
float Gy2[2];
float Angle2[2];


String valores,ax1,ay1,ax2,ay2;
long tiempo_prev;
float dt;
long tiempo_prev2 ;
float dt2;

void setup()
{
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(115200); 

  Wire.begin();
  Wire.beginTransmission(MPU2);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(115200);

}
void loop()
{
  //Leer los valores del Acelerometro de la IMU
  Wire.beginTransmission(MPU);
  Wire.write(0x3B); //Pedir el registro 0x3B - corresponde al AcX
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 6, true); //A partir del 0x3B, se piden 6 registros
  AcX = Wire.read() << 8 | Wire.read(); //Cada valor ocupa 2 registros
  AcY = Wire.read() << 8 | Wire.read();
  AcZ = Wire.read() << 8 | Wire.read();

  //Se calculan los angulos Y, X respectivamente. (primer IMU)
  Acc[1] = atan(-1 * (AcX / A_R) / sqrt(pow((AcY / A_R), 2) + pow((AcZ / A_R), 2))) * RAD_TO_DEG;
  Acc[0] = atan((AcY / A_R) / sqrt(pow((AcX / A_R), 2) + pow((AcZ / A_R), 2))) * RAD_TO_DEG;

 //Leer los valores del Giroscopio
  Wire.beginTransmission(MPU);
  Wire.write(0x43);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 6, true); //se piden 6 registros
  GyX = Wire.read() << 8 | Wire.read();
  GyY = Wire.read() << 8 | Wire.read();
  GyZ = Wire.read() << 8 | Wire.read();


  //Calculo del angulo del Giroscopio
  Gy[0] = GyX / G_R;
  Gy[1] = GyY / G_R;
  Gy[2] = GyZ / G_R;
  
  
  dt = (millis() - tiempo_prev) / 1000.0;
  tiempo_prev = millis();
  

  //Aplicar el Filtro Complementario
  Angle[0] = 0.7 * (Angle[0] + Gy[0] * 0.010) + 0.3 * Acc[0];
  Angle[1] = 0.7 * (Angle[1] + Gy[1] * 0.010) + 0.3 * Acc[1];

  //Integración respecto del tiempo paras calcular el YAW
  Angle[2] = Angle[2] + Gy[2] * dt;

  //Mostrar los valores por consola
  //Serial.print("Angle X: "); Serial.print(Angle[0]); Serial.print("\n");
  //Serial.print("Angle Y: "); Serial.print(Angle[1]); Serial.print("\n------------\n");

  //delay(10); //Nuestra dt sera, pues, 0.010, que es el intervalo de tiempo en cada medida



  Wire.beginTransmission(MPU2);
  Wire.write(0x3B); //Pedir el registro 0x3B - corresponde al AcX
  Wire.endTransmission(false);
  Wire.requestFrom(MPU2, 6, true); //A partir del 0x3B, se piden 6 registros
  AcX2 = Wire.read() << 8 | Wire.read(); //Cada valor ocupa 2 registros
  AcY2 = Wire.read() << 8 | Wire.read();
  AcZ2 = Wire.read() << 8 | Wire.read();

  //Se calculan los angulos Y, X respectivamente.(segundo IMU)
  Acc2[1] = atan(-1 * (AcX2 / A_R) / sqrt(pow((AcY2 / A_R), 2) + pow((AcZ2 / A_R), 2))) * RAD_TO_DEG;
  Acc2[0] = atan((AcY2 / A_R) / sqrt(pow((AcX2 / A_R), 2) + pow((AcZ2 / A_R), 2))) * RAD_TO_DEG;

 
  Wire.beginTransmission(MPU2);
  Wire.write(0x43);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU2, 6, true); //A diferencia del Acelerometro, solo se piden 4 registros  ( DEBO ESCOGER 6 PARA ANGULO Z)
  GyX2 = Wire.read() << 8 | Wire.read();
  GyY2 = Wire.read() << 8 | Wire.read();
  GyZ2 = Wire.read() << 8 | Wire.read();



  //Calculo del angulo del Giroscopio
  Gy2[0] = GyX2 / G_R;
  Gy2[1] = GyY2 / G_R;
  Gy2[2] = GyZ2 / G_R;
  
  dt2 = (millis() - tiempo_prev2) / 1000.0;
  tiempo_prev2 = millis();

  //Aplicar el Filtro Complementario
  Angle2[0] = 0.7 * (Angle2[0] + Gy2[0] * 0.010) + 0.3 * Acc2[0];
  Angle2[1] = 0.7 * (Angle2[1] + Gy2[1] * 0.010) + 0.3 * Acc2[1];

  //Integración respecto del tiempo paras calcular el YAW
  Angle2[2] = Angle2[2] + Gy2[2] * dt2;




  //Mostrar los valores por consola
  //Serial.print("Angle X2: "); Serial.print(Angle2[0]); Serial.print("\n");
  //Serial.print("Angle Y2: "); Serial.print(Angle2[1]); Serial.print("\n------------\n");

  //valores = String(Acc[1]) + " , " + String(Acc[0]);// + " , " + String(GyX) + " , " + String(GyY) + " , " + String(GyZ);

  valores = String(Angle[0]) + " , " + String(Angle[1]) + " , " + String(Angle[2])  + " , " + String(Angle2[0]) + " , " + String(Angle2[1]) +" , " + String(Angle2[2]);
  Serial.flush();
  Serial.println(valores);

  delay(210); //

  
}
