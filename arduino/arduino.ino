#define LED0 20
#define LED1 21
#define LED2 22
#define LED3 23
#define LED4 24
#define LED5 25
#define LED6 26
#define LED7 27
#define LED8 28
#define LED9 29
#define LED10 30
#define LED11 31
#define LED12 32
#define LED13 33
#define LED14 34
#define LED15 35
#define LED16 36
#define LED17 37
#define LED18 3

void setup() {
    pinMode(LED0, OUTPUT);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);
    pinMode(LED5, OUTPUT);
    pinMode(LED6, OUTPUT);
    pinMode(LED7, OUTPUT);
    pinMode(LED8, OUTPUT);
    pinMode(LED9, OUTPUT);
    pinMode(LED10, OUTPUT);
    pinMode(LED11, OUTPUT);
    pinMode(LED12, OUTPUT);
    pinMode(LED13, OUTPUT);
    pinMode(LED14, OUTPUT);
    pinMode(LED15, OUTPUT);
    pinMode(LED16, OUTPUT);
    pinMode(LED17, OUTPUT);
    pinMode(LED3, OUTPUT);

    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == '0') {
            digitalWrite(LED0, HIGH);
        }
        if (serialListener == '1') {
            digitalWrite(LED1, HIGH);
        }
        else if (serialListener == '2') {
            digitalWrite(LED2, HIGH);
        
        }
        else if (serialListener == '3') {
            digitalWrite(LED3, HIGH);
        }
              
        else if (serialListener == '4') {
            digitalWrite(LED4, HIGH);
        }
        else if (serialListener == '5') {
            digitalWrite(LED5, HIGH);
        }
        else if (serialListener == '6') {
            digitalWrite(LED6, HIGH);
        }
        else if (serialListener == '7') {
            digitalWrite(LED7, HIGH);
        }
        else if (serialListener == '8') {
            digitalWrite(LED8, HIGH);
        } 
        else if (serialListener == '9') {
            digitalWrite(LED9, HIGH);
        } 
        else if (serialListener == 't') {
            digitalWrite(LED10, HIGH);
        } 
        else if (serialListener == 'e') {
            digitalWrite(LED11, HIGH);
        } 
        else if (serialListener == 'w') {
            digitalWrite(LED12, HIGH);
        }
        else if (serialListener == 'h') {
            digitalWrite(LED13, HIGH);
        } 
        else if (serialListener == 'o') {
            digitalWrite(LED14, HIGH);
        } 
        else if (serialListener == 'i') {
            digitalWrite(LED15, HIGH);
        } 
        else if (serialListener == 'x') {
            digitalWrite(LED16, HIGH);
        } 
        else if (serialListener == 'v') {
            digitalWrite(LED17, HIGH);
        }  
        else if (serialListener == 'z') {
            digitalWrite(LED18, HIGH);
        }  
        else if (serialListener == ')') {
            digitalWrite(LED0, LOW);
        }
        else if (serialListener == '!') {
            digitalWrite(LED1, LOW);
        }
        else if (serialListener == '@') {
            digitalWrite(LED2, LOW);

        }
        else if (serialListener == '#') {
            digitalWrite(LED3, LOW);
        }
        else if (serialListener == '$') {
            digitalWrite(LED4, LOW);
        }
        else if (serialListener == '%') {
            digitalWrite(LED5, LOW);
        }
        else if (serialListener == '^') {
            digitalWrite(LED6, LOW);
        }
        else if (serialListener == '&') {
            digitalWrite(LED7, LOW);
        }
        else if (serialListener == '*') {
            digitalWrite(LED8, LOW);
        } 
        else if (serialListener == '(') {
            digitalWrite(LED9, LOW);
        } 
        else if (serialListener == 'T') {
            digitalWrite(LED10, LOW);
        } 
        else if (serialListener == 'E') {
            digitalWrite(LED11, LOW);
        } 
        else if (serialListener == 'W') {
            digitalWrite(LED12, LOW);
        }
        else if (serialListener == 'H') {
            digitalWrite(LED13, LOW);
        }
        else if (serialListener == 'O') {
            digitalWrite(LED14, LOW);
        }
        else if (serialListener == 'I') {
            digitalWrite(LED15, LOW);
        }
        else if (serialListener == 'X') {
            digitalWrite(LED16, LOW);
        }
        else if (serialListener == 'V') {
            digitalWrite(LED17, LOW);
        }
        else if (serialListener == 'Z') {
            digitalWrite(LED18, LOW);
        }
    }
}


