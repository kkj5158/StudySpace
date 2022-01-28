package lib.figure;

import java.awt.Color;
import java.awt.Graphics;

public class ColorRect {

	private int leftupperx;
	private int leftuppery;
	private int rightdownx;
	private int rightdowny;
	
	private int width;
	private int height;
	
	private Color color;
	
	

	public ColorRect() {
		leftupperx = 100;
		leftuppery = 100;
		rightdownx = 200;
		rightdowny = 200;
	}

	public ColorRect(int lux, int luy, int rdx, int rdy) {
		leftupperx = lux;
		leftuppery = luy;
		rightdownx = rdx;
		rightdowny = rdy;
	}

	public int getWidth() {
		return width;
	}

	public void setWidth(int width) {
		this.width = width;
	}

	public void setWidth() {
		this.width = rightdownx - leftupperx;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	public int getHeight() {
		return height;
	}

	public void setHeight() {
		this.height = rightdowny - leftuppery;
	}

	public int getLeftupperx() {
		return leftupperx;
	}

	public void setLeftupperx(int leftupperx) {
		this.leftupperx = leftupperx;
	}

	public int getLeftuppery() {
		return leftuppery;
	}

	public void setLeftuppery(int leftuppery) {
		this.leftuppery = leftuppery;
	}

	public int getRightdownx() {
		return rightdownx;
	}

	public void setRightdownx(int rightdownx) {
		this.rightdownx = rightdownx;
	}

	public int getRightdowny() {
		return rightdowny;
	}

	public void setRightdowny(int rightdowny) {
		this.rightdowny = rightdowny;
	}
	
	
	public Color getColor() {
		return color;
	}

	public void setColor(Color color) {
		this.color = color;
	}

	public void sizeUP(int width, int height) {
		this.width = this.width + width;
		this.height = this.height + height;

	}

	public void draw(Graphics g) {
		g.setColor(color);
		g.drawRect(leftupperx, leftuppery, width, height);
	}

	public boolean checkRectIn(int x, int y) {

		boolean xIn = this.leftupperx <= x && this.leftupperx+this.width >= x;
		boolean yIn = this.leftuppery <= y && this.leftuppery+this.height >= y;

		return xIn && yIn;
	}

}
