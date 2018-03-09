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
public class Room {
    int width, height, anchorX, anchorY;
    int[] xVals, yVals;
    Encounter[] encounters;
    
    public Room(){
        
    }
    
    public Room(int dimX, int dimY, int X, int Y){
        // set width and height
        width = dimX;
        height = dimY;
        // set anchor points
        anchorX = X;
        anchorY = Y;
        // create array of x values, since square, this method works, will need
        // to be upated if weird shaped rooms allowed
        xVals = new int[dimX];
        yVals = new int[dimY];
        
        //populate array of X and Y values
        int j = 0;
        while (j<dimX){
            int x = j+anchorX;
            xVals[j] = x;
            j++;
        }
        int i = 0;
        while (i<dimY){
            int y = i+anchorY;
            yVals[i] = y;
            i++;
        }
    }
    
    public void createEncounter(){
        
    }
    
    public void fillRoom(){
        
    }
    
}
