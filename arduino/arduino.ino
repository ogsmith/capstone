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

// Boolean that switches states (hard on off)
// Defaults on pins that are currently in model
// Main loop that controls amount of time they're on and off
//
//

// Code inspired from https://forum.arduino.cc/index.php?topic=137920.0
class Pulse
{
    byte _ledPin;                                                  
    boolean _ledOn;                                                
    unsigned long _lastToggle;                              
    unsigned long _duration;                                       

public:
    unsigned long onDuration;                                      
    unsigned long offDuration;                                     
    boolean pulse;                                              

    Pulse(byte);                                               
    void begin(unsigned long, unsigned long);                      
    boolean check(void);                                        
};

Pulse::Pulse(byte pin)
{
    _ledPin = pin;
    _lastToggle = 0;
    _duration = 0;
    _ledOn = false;
    pulse = false;
}

void Pulse::begin(unsigned long on, unsigned long off)
{
    pinMode(_ledPin, OUTPUT);                                 
    onDuration = on;
    offDuration = off;
}

boolean Pulse::check()
{
    if (!pulse) return false;                                    
    if (millis() - _lastToggle > _duration)                  
    {
        if (_ledOn)                                                
        {
            digitalWrite (_ledPin, LOW);                          
            _ledOn = false;                                        
            _lastToggle = millis();                        
            _duration = offDuration;                              
        }
        else
        {
            digitalWrite (_ledPin, HIGH);                         
            _ledOn = true;                                        
            _lastToggle = millis();                          
            _duration = onDuration;                               
        }
    }
    return true;
}

                                 


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
        char serialListener = Serial.read();;
        char message[15]; 
        int i = 0;
        
//        while (&serialListener != "e") {
//          serialListener = Serial.read();
//          message[i] = serialListener;
//          i = i+1;
//          Serial.println(serialListener);
//        }

      Serial.println(serialListener);
//        if (serialListener == '0') {
//            Pulse turn_on(0); 
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;        
//        }
//        if (serialListener == '1') {
//            Pulse turn_on(1); 
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;   
//        }
//        else if (serialListener == '2') {
//            Pulse turn_on(2);  
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;  
//        }
//        else if (serialListener == '3') {
//            Pulse turn_on(3);  
//            turn_on.begin(.2, 500);  
//            turn_on.pulse = true;  
//        }
//              
//        else if (serialListener == '4') {
//            Pulse turn_on(4);  
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true; 
//            turn_on.check();
//        }
//        else if (serialListener == '5') {
//            Pulse turn_on(5);
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;    
//        }
//        else if (serialListener == '6') {
//            Pulse turn_on(6);  
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;  
//        }
//        else if (serialListener == '7') {
//            Pulse turn_on(7); 
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;   
//        }
//        else if (serialListener == '8') {
//            Pulse turn_on(8);  
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;  
//        } 
//        else if (serialListener == '9') {
//            Pulse turn_on(9);  
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;  
//        } 
//        else if (serialListener == 't') {
//            Pulse turn_on(10);  
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;  
//        } 
//        else if (serialListener == 'e') {
//            Pulse turn_on(11); 
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;   
//        } 
//        else if (serialListener == 'w') {
//            Pulse turn_on(12);  
//            turn_on.begin(.2, 500); 
//            turn_on.pulse = true;  
//        } 
//        else if (serialListener == ')') {
//            digitalWrite(LED0, LOW);
//        }
//        else if (serialListener == '!') {
//            digitalWrite(LED1, LOW);
//        }
//        else if (serialListener == '@') {
//            digitalWrite(LED2, LOW);
//        }
//        else if (serialListener == '#') {
//            digitalWrite(LED3, LOW);
//        }
//        else if (serialListener == '$') {
//            digitalWrite(LED4, LOW);
//        }
//        else if (serialListener == '%') {
//            digitalWrite(LED5, LOW);
//        }
//        else if (serialListener == '^') {
//            digitalWrite(LED6, LOW);
//        }
//        else if (serialListener == '&') {
//            digitalWrite(LED7, LOW);
//        }
//        else if (serialListener == '*') {
//            digitalWrite(LED8, LOW);
//        } 
//        else if (serialListener == '(') {
//            digitalWrite(LED9, LOW);
//        } 
//        else if (serialListener == 'T') {
//            digitalWrite(LED10, LOW);
//        } 
//        else if (serialListener == 'E') {
//            digitalWrite(LED11, LOW);
//        } 
//        else if (serialListener == 'W') {
//            digitalWrite(LED12, LOW);
//        }
    }
    
}

