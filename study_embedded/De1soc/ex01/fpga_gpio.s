.global _start
_start:
	LDR R0, =0xFF200000 // Red LED
	LDR R1, =0xFF200040 // Switch
LOOP:
	LDR R3, [R1] // read Switch
	STR R3, [R0] // write to LED
	B LOOP
END: B END

.end 
	