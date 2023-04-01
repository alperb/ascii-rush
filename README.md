# pixel-rush

### Challenge Details

**Name:** ASCII Rush  
**Category:** Coding  
**FLAG:** `SUCTF{TcP_1s_r34lly_Aw3s0m3}`  
**Description:**  
You need to find your way out of this labyrinth. You need to open a TCP connection to `URL HERE`. In order
to start playing you need to send `START` message to the server. Then server will send you a labyrinth piece looking
like this:   
|======= ==|   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|   
| =========|

The bottom spot is the place where you will start and the top blank spot is the exit of this piece.
You need to answer to the server with the amount of characters you need to walk to go the exit from the entrance.
If you walk right, then you are walking to positive. If you walk left, then you are walking to negative.

For example, the above example's answer will be 7 since it requires 7 steps to the right to reach the exit.

You need to send the server `ANS 7` as the response.

In some piece you won't see a blank spot on top, instead you'll see a character. Like this:   

|==X=======|   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|   
|======= ==|

X will be the next character of the flag. You need to collect the characters along the way.

Good luck!  

