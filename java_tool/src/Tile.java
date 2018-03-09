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
public class Tile {
    String type;
    String textValue;
    
    public Tile(){
        
    }
    
    public Tile(String nodeType){
        type = nodeType;
    }
    
    public String getText(){
        updateTextValue();
        return textValue;
    }
    
    public void updateTextValue(){
        if (type == "solid"){
            textValue = "X";
        }else{
            textValue = " ";
        }
    }
    
    public String[] gridTextOut(){
        String[] grid = new String[3];
        grid[0] = "+-+";
        grid[1] = "|" + textValue +"|";
        grid[2] = "+-+";
        
        
        return grid;
    }
    
}
