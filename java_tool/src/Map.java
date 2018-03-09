/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dnd_tools;
import java.util.concurrent.ThreadLocalRandom;
import java.util.*;

/**
 *
 * @author ryanbomo
 */
public class Map {
    int mapX;
    int mapY;
    Tile[][] tiles;
    ArrayList<Room> rooms = new ArrayList<Room>();
    Hallway[] halls;
    
    public Map(int X, int Y){
        mapX = X;
        mapY = Y;
        tiles = new Tile[mapY][mapX];
        for(int i = 0; i < mapX;i++){
            for(int j = 0;j<mapY;j++){
                tiles[j][i] = new Tile("solid");
            }
        }
    }
    
    private int randomInt(int a, int b){
        int rand = ThreadLocalRandom.current().nextInt(a, b + 1);
        return rand;
    }
    
    public void makeRooms(int attempts){
        // Get Max Room Height (Y)
        Double max_D = (.4*mapY);
        int maxRoomHeight = max_D.intValue();
        if(maxRoomHeight >20){
            maxRoomHeight = 20;
        }
        
        //Get Max Room Width (X)
        max_D = (.4*mapX);
        int maxRoomWidth = max_D.intValue();
        if(maxRoomWidth >20){
            maxRoomWidth = 20;
        }
        
        // create rooms
        for (int i = 0;i<attempts;i++){
        
            // create random height
            int randHeight = randomInt(2, maxRoomHeight);
            // create random width
            int randWidth = randomInt(2, maxRoomWidth);
            // get max X,Y anchor coords
            int maxY = mapY - randHeight;
            int maxX = mapX - randWidth;
            // create random X,Y anchor coords using maximums
            int yCoord = randomInt(0, maxY);
            int xCoord = randomInt(0, maxX);
            // create room
            Room temp = new Room(randWidth,randHeight,xCoord,yCoord);
            
            //collision detect
            boolean isValid = collisionDetection(temp);
            
            
            if (isValid){
                //if pass, create room
                rooms.add(temp);
                // set tiles
                for (int y : temp.yVals){
                    for(int x: temp.xVals){
                        tiles[y][x].type = "open";
                
                    }

                }

            }
        }
    }
    
    private boolean collisionDetection(Room roomToTest) {
        boolean isValid = true;
        //collision detect
        if (!rooms.isEmpty()) {
            for (Room r : rooms) {
                Boolean xBool = false;
                Boolean yBool = false;
                for (int xvalTemp : roomToTest.xVals) {
                    for (int xvalR : r.xVals) {
                        xBool = (xvalTemp == xvalR);
                        if (xBool) {
                            break;
                        }
                    }
                    if (xBool) {
                        break;
                    }
                }

                for (int yvalTemp : roomToTest.yVals) {
                    for (int yvalR : r.yVals) {
                        yBool = (yvalTemp == yvalR);
                        if (yBool) {
                            break;
                        }
                    }
                    if (yBool) {
                        break;
                    }

                }
                if (yBool && xBool) {
                    isValid = false;
                }
            }
        }
        return isValid;
    }
  
    
    public void makeHalls(){
        // create graph connecting all rooms to each other with paths weighted by room distances
        // figure out interesting way to then make these hallways
        
    }
    
    public int[][] getMap(){
        int[][] map = new int[mapY][mapX];
        int lilx = 0;
        int lily = 0;
        for (Tile[] i : tiles){
            for (Tile j : i){
                if (j.type == "wall"){
                    map[lily][lilx] = 1;
                }else{
                    map[lily][lilx] = 0;
                }
                lilx++;
            }
            lily++;
            lilx = 0;
        }
        return map;
    }
    
    public void drawMap(){
        for (Tile[] i : tiles){
            String output = "";
            for (Tile j : i){
                output = output + j.getText();
            }
            System.out.println(output);
        }
        
    }
    
    
    //Not workign correctly
    /*
    public void drawDetailedMap(){
        for (Tile[] i : tiles){
            String output1 = "";
            String output2 = "";
            String output3 = "";
            for (Tile j : i){
                String[] grid = j.gridTextOut();
                output1 = output1 + grid[0];
                output2 = output2 + grid[1];
                output3 = output3 + grid[2];
            }
            System.out.println(output1);
            System.out.println(output2);
            System.out.println(output3);
        }
        
    }
    */
    
}
