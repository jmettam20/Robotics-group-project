
#include <stdio.h>
#include <wiringPi.h>

#define LED 1

int main(void){
	printf("Blinky Blink");
	
	wiringPiSetup(); 
	pinMode(LED, OUTPUT); 
	
	for(;;){
		digitalWrite(LED, HIGH);
		delay(500);
				digitalWrite(LED, LOW);
		delay(500);
		}
		return 0;
	}
