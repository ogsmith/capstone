void setup() {
    Serial.begin(9600);
    pinMode(20, OUTPUT);
    pinMode(21, OUTPUT);
    pinMode(22, OUTPUT);
    pinMode(23, OUTPUT);
    pinMode(24, OUTPUT);
    pinMode(25, OUTPUT);
    pinMode(26, OUTPUT);
    pinMode(27, OUTPUT);
    pinMode(28, OUTPUT);
    pinMode(29, OUTPUT);
    pinMode(30, OUTPUT);
    pinMode(31, OUTPUT);
    pinMode(31, OUTPUT);
    pinMode(32, OUTPUT);
    pinMode(33, OUTPUT);
    pinMode(34, OUTPUT);
    pinMode(35, OUTPUT);
    pinMode(36, OUTPUT);
    pinMode(37, OUTPUT);
    pinMode(38, OUTPUT);
}

  bool bool_val = true;
  String write_to = String("");
  String delay_set = String("");
  String delays;
  float pulse_lengths[14];
  String wave_length = String("");
  float wave = 0;
  String message = String("");
  float delay_val = 0;
  int d = 0;
  int ports[14];
  String port_number = String("");
  int p = 0;
  int port_val = 0;
  
void configure_ports(char ser){

  if (ser == 'd') {
        write_to = "delays";
   }
  else if (ser == 'w'){
        write_to = "wave_length";
  }
  else if (ser == 'p'){
        write_to = "ports";
  }
  else if(ser == 'e'){
        delay_val = delays.toFloat();
        pulse_lengths[d] = delay_val;
        d = d+1;
        delays = "";
  }
  else if (ser == 't'){
    if(ports[14] == 0) {
       port_val = port_number.toInt();
       ports[p] = port_val;
       p = p + 1;
//       Serial.println(ports[p]);
       port_number = ""; 
    }  
  }
  else if (ser == 'l'){
    wave = wave_length.toFloat();
    wave_length = "";
    p = 0;
    d = 0;
    bool_val = false;
  }
  else {
     if (write_to == "delays"){
         delays += ser;
      }
     if (write_to == "wave_length"){
         wave_length += ser;
         
      }
     if (write_to == "ports"){
         port_number+=ser;
     }
  }
}

void digitalWriteLow(int pin, float pulse) {
    digitalWrite(pin, LOW);
//    Serial.println("ports:"+ String(pin));
    delayMicroseconds(pulse);
//    Serial.println("pulse lengths" + String(pulse)); 
}

void loop() {    
    if (Serial.available()) {
        char serialListener = Serial.read();
        configure_ports(serialListener);
        while(bool_val){
              if (Serial.available()) {
                  char serialListener = Serial.read();
                  configure_ports(serialListener);
               } else{
                     bool_val = false;
               }
          
        }
        bool_val = true;
    }
    

 for(int i=0; i< 14; i++){
    digitalWriteLow(ports[i], pulse_lengths[i]); 
 }
  
    
    Serial.println(wave);
   delayMicroseconds(wave);
    for (int i=0; i < 14; i++){
      digitalWrite(ports[i], HIGH);
    }
}

