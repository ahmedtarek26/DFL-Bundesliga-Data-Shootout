# DFL Bundesliga DataShootout
Competition link : https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout

## Events descripsion

### Sample of results

<div align=center>
          <img alt="gif" align="center" src="sample-result.gif"/>
    </div>
    
### Plays
A Play describes a player’s attempt to switch ball control to another member of his team. A play event may be executed as a Pass or as a Cross.

Whether a play is a Cross depends upon the positions of the acting player and of the possible recipient. The player playing the cross must be located approx. inside one of the four crossing zones. The four zones are marked by the touchlines, the extended sides of the penalty area, the goal lines and the imaginary quarter-way lines, which would be drawn at a quarter of the length of the pitch parallel to the half-way line (see figure below). The possible cross recipient must be located approx. inside the penalty area. Furthermore, the distance of the ball played must be medium-length (from 10 to 30 meters) or long (more than 30 meters) and the height of the ball played must be high (played above knee height). In order to classify a ball played as a cross if the ball is blocked by an opposing player, it is not the actual height or distance travelled that is decisive, but the intended height or distance.

The second type of play is a Pass, defined to be any attempt to switch ball control to another team member that doesn’t satisfy cross definition.

Additionally, every Play action (both Pass and Cross) is executed in within a context, making it an Open Play, a Corner Kick, or a Free Kick.

A Corner Kick refers to a situation where the Play is executed to restart the game after the ball went out of play over the goal line following the touch of the defending team player. The ball must be kicked from the closest field corner and be stationary on the ground when it’s kicked off.

A Free Kick refers to a situation where the Play is executed to restart the game after the referee had stopped it due to an infringement of the rules. The ball must be kicked and be stationary on the ground when it's kicked off.

An Open Play refers to any Play that is executed in-play and not from a dead ball situation (like corner kick, free kick or any other set piece).

### Throw-Ins
A Throw-In refers to a situation where the game is restarted after the ball went out of play over the sideline following the touch of the opposite team. The ball must be thrown with hands, from behind and over the head of executing player.

### Challenge
A Challenge is a player action during which two players of opposing teams are physically capable of either gaining or receiving ball control and attempt to do so. A Challenge requires one of the two players to touch the ball or to foul the opposing player.

A distinction is made between the following cases:

Opponent rounded: a player in ball control stays in ball control after the challenge, having left the opposing player behind him. Situations where the opponent is not able to gain possession (e.g. when the ball is “flicked” over the opponent) are also to be recorded as challenges.
Ball action carried out: applies when none of the players involved in the challenge are in ball control at the start of the challenge (e.g. aerial challenges, challenges for the first touch of the ball) and one player determines the direction of the ball at the end of the challenge.
Fouled: the referee called a foul.
Opponent dispossessed: a player not in ball control dispossesses the opposing player in ball control.
Challenge during release of the ball: applies when shots or balls played are forced or blocked during challenges. A challenge is only recorded, if the ball played or shot travels through the area that the defending player is attempting to cover from a tactical perspective. All other cases are not recorded as challenges.
Possession retained during challenge: applies when one of the players involved in the challenge has certain ball control at the start of the challenge and manages to retain it, despite the efforts to dispossess him of the opponent involved in the challenge.


