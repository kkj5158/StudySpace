.global _start
_start:
	
	mov r0, #0x10
	mov r1, #0x20
	mov r2, #0
	add r3, r0, r1
	sub r4, r0, r1
	movlt r2, #1
	subs r4, r0, r1
	movlt r2, #2
	rsb r4, r0, r1
	movlt r2, #3
	rsbs r4, r0, r1
	movlt r2, #4
stop:
	b stop 