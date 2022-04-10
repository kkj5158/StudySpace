.global _start
_start:
	mov r0, #0x75
	and r1, r0, #0xffffffcf
	orr r2, r0, #0b1100
	EOR r3, r0, #0b11
	mvn r4, r0 
	
	teq r0, r4 // 같으면 z=1 
	addne r4, r4, #0b1
	
	smulls r6 ,r5, r0, r4 // 만약 r0*r4 의 결과가 음수이면 n이 1로 설정된다. 
	addmi r0, r0, #0b1 // n=1 이면 덧셈 수행 
	
stop:
	b stop 