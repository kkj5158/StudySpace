//	Find	the	sum	of	numbers	from	0	to	N	
/*	Equivalent	C	code	function	would	be:
int	FINDSUM(int	N)
{
int	sum	=	0;
while	(N	>	0)	{
sum	=	sum	+	N;
N	=	N	-	1;
}
return	sum;
}
*/
.text
.global _start
_start:
LDR R0,	N
BL FINDSUM
END: B END

//	FINDSUM	subroutine:	calculates	the	sum	of	numbers	from	1	to	N
// Parameters:	R0	=	N
// Returns:	R0	=	sum

FINDSUM:
MOVS R1,	R0 //	R1	:	N
MOV R0,	#0 //	R0	:	sum
SUM_LOOP:
BLE END_LOOP //	if	(N	<=0)	goto	end_loop
ADD R0,	R0,	R1 //	sum	=	sum	+	N
SUBS R1,	#1 //	N	=	N	-	1
B SUM_LOOP
END_LOOP: //	R0	:	sum
MOV PC,	LR //	return
N: .word 5
.end