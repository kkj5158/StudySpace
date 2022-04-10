.global	_start
_start:	
//	shifted	operand
	mov	r0,	#0x10 //	r0
	mov	r1,	#4 //	r1
	mov	r2,	r0,	lsl	#3 //	r2,	
	lsl	r2,	r0,	#3 //	앞명령어와	비교
	mov	r3,	r0,	lsr	r1 //	r3,	
	lsr	r3,	r0,	r1 //	앞명령어와	비교
	mov	r0,	#-8 //	r0
	mov	r4,	r0,	asl	#2 //	r4,	lsl을	사용한	경우와	비교
	mov	r5,	r0,	asr	#3 //	r5
	asr	r5,	r0,	#3 //	앞명령어와	비교
	mov	r6,	r0,	lsr	#3
//	multiplication	using	shifted	operand
	mov	r0,	#10
	add	r1,	r0,	r0,	lsl	#2 //	r1	=	r0*5	=	r0*(1+4)
	rsb	r2,	r0,	r0,	lsl	#4 //	r2	=	r0*15	=	r0*(16-1)
	rsb	r2,	r2,	r2,	lsl	#3 //	r2	=	r2*7	=	r2*(8-1)
//	multiplication
	mov	r0,	#10
	mov	r1,	#15
	mul	r2,	r0,	r1 //	r2	=	r0	*	r1
	mov	r4,	#4;
	mla	r2,	r4,	r4,	r2 //	r2	=	r2	+	r4*r4
	mov	r0,	#0x80000001
	mov	r1,	#8
	mul	r2,	r0,	r1 //	r2,	multiply
	umull	r3,	r4,	r0,	r1 //	r3,r4,	multiply-long	(unsigned)
	smull	r5,	r6,	r0,	r1 //	r5,r6,	multiply-long	(signed)
stop:	
	b	stop
