.global	_start
_start:	
	mov	r0,	#data1 //	r0,	data1의	주소	확인
	ldr	r1,	[r0] //	r1
	
	ldr	r2,	[r0,#4] //	r2,	r0,	메모리	주소
	ldr	r3,	[r0],#4 //	r3,	r0,	메모리	주소
	ldr	r4,	[r0,#4]! //	r4,	r0,	메모리	주소
	ldr	r0,	=#data1 //	r0
	
	mov	r1,	#12
	ldr	r5,	[r0,	r1] //	r5,	메모리	주소	
	
	mov	r1,	#3
	ldr	r6,	[r0,r1,	lsl	#2]		//		r6,	메모리	주소
stop:	
	b	stop
data1: .word	1,	2,	3,	4,	5,	6,	7,	8