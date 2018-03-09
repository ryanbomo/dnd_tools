/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dnd_tools;

/**
 *
 * @author ryanbomo
 */
public class Hallway {
    int startX;
    int startY;
    int endX;
    int endY;
    
    public Hallway(){
        
    }
    
    public Hallway(int beginX, int beginY, int finalX, int finalY){
        startX = beginX;
        startY = beginY;
        endX = finalX;
        endY = finalY;
    }
    
}
