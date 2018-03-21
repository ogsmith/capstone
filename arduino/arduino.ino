#define LED0 0
#define LED1 1
#define LED2 2
#define LED3 3
#define LED4 4
#define LED5 5
#define LED6 6
#define LED7 7
#define LED8 8
#define LED9 9
#define LED10 10
#define LED11 11
#define LED12 12


// Using http://slides.justen.eng.br/python-e-arduino as refference

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
//            digitalWrite(LED2, HIGH);
            PORTD |= _BV(LED2);
        }
        else if (serialListener == '3') {
            digitalWrite(LED3, HIGH);
//              PORTD |= _BV (3);        
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
        else if (serialListener == ')') {
            digitalWrite(LED0, LOW);
        }
        else if (serialListener == '!') {
            digitalWrite(LED1, LOW);
        }
        else if (serialListener == '@') {
//            digitalWrite(LED2, LOW);
            PORTD &= ~_BV(LED2);
        }
        else if (serialListener == '#') {
            digitalWrite(LED3, LOW);
//            PORTD &= ~_BV (3);        
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
    }
}


