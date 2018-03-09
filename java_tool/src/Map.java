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
        tiles = new Tile[mapY][mapX];
        for(int i = 0; i < mapX;i++){
            for(int j = 0;j<mapY;j++){
                tiles[j][i] = new Tile();
            }
        }
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
    
    public int[][] returnMap(){
        int[][] map = new int[mapY][mapX];
        int lilx = 0;
        int lily = 0;
        for (Tile[] i : tiles){
            for (Tile j : i){
                if (j.isSolid){
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
        int x = 0,y = 0;
        String topLine = " ";
        while (x<mapX){
            if (x<10){
                topLine = topLine +"  "+ x;
            }else{
                topLine = topLine + " " +x;
            }
            x++;
        }
        System.out.println(topLine);
        
        for (Tile[] i : tiles){
            String count = ""+y;
            if (y<10){
                count = " " + count;
            }
            String output = count;
            for (Tile j : i){
                output = output + j.getText();
            }
            System.out.println(output);
            y++;
        }
        
    }
    
}
