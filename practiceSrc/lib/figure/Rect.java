package lib.figure;

import java.awt.Color;
import java.awt.Graphics;

public class Rect {
	
	protected int upperLeftX;
	protected int upperLeftY;
	protected int lowerRightX;
	protected int lowerRightY;
	
	public Rect() {
		upperLeftX = 100;
		upperLeftY = 100;
		lowerRightX = 150;
		lowerRightY = 170;
	}
	
	public Rect(int ulx, int uly, int lrx, int lry) {
		upperLeftX = ulx;
		upperLeftY = uly;
		lowerRightX = lrx;
		lowerRightY = lry;
	}

	public int getUpperLeftX() {
		return upperLeftX;
	}

	public void setUpperLeftX(int upperLeftX) {
		this.upperLeftX = upperLeftX;
	}

	public int getUpperLeftY() {
		return upperLeftY;
	}

	public void setUpperLeftY(int upperLeftY) {
		this.upperLeftY = upperLeftY;
	}

	public int getLowerRightX() {
		return lowerRightX;
	}

	public void setLowerRightX(int lowerRightX) {
		this.lowerRightX = lowerRightX;
	}

	public int getLowerRightY() {
		return lowerRightY;
	}

	public void setLowerRightY(int lowerRightY) {
		this.lowerRightY = lowerRightY;
	}
	

	public void moveTo(int ulx, int uly) {
		int width = lowerRightX - upperLeftX;
		int height = lowerRightY - upperLeftY;
		upperLeftX = ulx;
		upperLeftY = uly;
		lowerRightX = ulx + width;
		lowerRightY = uly + height;
	}

	public void draw(Graphics g) {
		g.setColor(Color.blue);
		int width = lowerRightX - upperLeftX;
		int height = lowerRightY - upperLeftY;
		g.drawRect(upperLeftX, upperLeftY, width, height);
	}
	
	public boolean includes(int x, int y) {
		if((upperLeftX<x) && (lowerRightX>x))
			if((upperLeftY<y) && (lowerRightY>y))
				return true;
		return false;
	}
	
	
	
}