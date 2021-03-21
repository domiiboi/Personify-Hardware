#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <wiringPi.h>
int main() {
	wiringPiSetupGpio();
	int buzzer = 18;
	int sensor = 16;
	int LED1 = 21;
	pinMode(buzzer, OUTPUT);
	pinMode(sensor, INPUT);
	int Toggle = 1;
	while (true){
		if(Toggle){
			printf("\n");
			printf("GPIO.input(sensor) \n");
			printf("GPIO.output(buzzer, True) \n");
			//digitalWrite(buzzer, HIGH);
			digitalWrite(LED1, HIGH);
			printf("Object Detected \n");
			printf("data = {\"proximity\":1}");
			printf("db.child(\"PIR\").set(data)");
			sleep(2);
			Toggle = 0;
		}
		else{
			printf("\n");
			printf("condition false");
			//digitalWrite(buzzer, LOW);
			digitalWrite(LED1, LOW);
			sleep(2);
			Toggle =1;
		}
	}
	return 0;
}



