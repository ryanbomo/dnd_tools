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
public class DND_tools {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int x = 23;
        int y = 20;
        Map newMap = new Map(x,y);
        int[][] map = newMap.getMap();
        newMap.makeRooms(15);
        newMap.drawMap();
        
    }
    
}
