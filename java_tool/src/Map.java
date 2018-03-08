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
public class Map {
    int mapX;
    int mapY;
    Tile[][] tiles;
    Room[] rooms;
    Hallway[] halls;
    
    public Map(int X, int Y){
        mapX = X;
        mapY = Y;
    }
    
    public void blankMap(){
        //Create All tiles
        //set each tile to isSold = True
    }
    
    public void makeRooms(){
        // Rooms have size properties and an anchor point
        // Generate Rooms
            // Collision Detection
        // for room in rooms[]:
        //      for x in range(roomX):
        //          for y in range(roomY):
        //              tiles[y][x].isSolid = False;
    }
    
    public void makeHalls(){
        // create graph connecting all rooms to each other with paths weighted by room distances
        // figure out interesting way to then make these hallways
        
    }
    
    public void drawMap(){
        
    }
    
}
