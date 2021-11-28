// Written by Aaron Barge
// Copyright 2021


// Includes
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif


// Defines
#define LED_PIN   11
#define LED_COUNT 50


// Global Variables
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_RGB + NEO_KHZ800);
uint8_t led_count = 0, index = 0, red = 0, green = 0, blue = 0;


// Helper Functions
void request_n_bytes(uint8_t bytes) {
  Serial.write(bytes);
}


uint8_t wait_for_uint8_t() {
  while (Serial.available() <= 0);
  if (Serial.available() > 0)
    return 0xff & Serial.read();
  return 0;
}


// Setup
void setup() {
#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif
  strip.begin();                  // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();                   // Turn OFF all pixels ASAP
  strip.setBrightness(255);       // Set BRIGHTNESS to max
  Serial.begin(115200);            // Turn on serial
  delay(500);
  char data = wait_for_uint8_t(); // Wait for python dummy byte
  if (data != 'a') {              // Check that the dummy byte was transmitted correctly
    Serial.write("Fail.");
    exit(0);
  }
  Serial.write("begin");          // Tell python the arduino is ready
  delay(5000);
}


// Main Loop
void loop() {
  request_n_bytes(1);
  led_count = wait_for_uint8_t();  
  for (size_t i = 0; i < led_count; ++i) { // for each LED index, color pair
    index = wait_for_uint8_t();            // grab and set colors at index
    red = wait_for_uint8_t();
    green = wait_for_uint8_t();
    blue = wait_for_uint8_t();
    strip.setPixelColor(index, strip.Color(red, green, blue));
  }
  strip.show();                            // show color strip
}
