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
    Boolean isSolid;
    String[] contains;
    String textValue;
    
    public Tile(){
        isSolid = true;
    }
    
    public String getText(){
        updateTextValue();
        return textValue;
    }
    
    public void updateTextValue(){
        if (isSolid){
            textValue = "[X]";
        }else{
            textValue = "[ ]";
        }
    }
    
}
