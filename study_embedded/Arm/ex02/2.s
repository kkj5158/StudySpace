.global	_start
_start:	
	mov	r0,	#src //	r8,	src	주소	확인
	mov	r1,	#dst //	r9,	dst	주소
	ldmia	r0,	{r2-r9} //	r0,	r2-r9
	stmia	r1!,{r2-r9} //	r1,	dst	메모리	블록	내용
	mov	sp,	#tos //	sp,	tos	주소	확인
	stmfd	sp!,	{r2-r9}	 //	sp,	스택메모리
	ldmfd	sp!,	{r2-r9} //	sp,	r5-r9
	mov	sp,	#tos
	push	{r2-r4} //	sp,	스택메모리
	pop	{r10-r12} //	sp,	r10-r12
stop:	
	b	stop
	
src: .word	0x1111,	0x2222,	0x3333,	0x4444,	0x5555,	0x6666,	0x7777,	0x8888
dst: .space	20
stack:	 .space	256
tos: //	top	of	stack