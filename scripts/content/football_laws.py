# Football: Laws & Officiating — 77 questions, applied-reasoning style.
# Framed around scenarios a referee/player would actually face, not bare recall.
QUESTIONS = [
{
 "q": "A defender is the last player between the striker and the goalkeeper when a teammate plays the striker through, but the striker was already level with the defender (not ahead of them) at the moment the ball was played. What should the assistant referee signal?",
 "options": [
   "No offside — a player is only offside if they are nearer to the opponents' goal line than both the ball and the second-last opponent at the moment the ball is played, and being exactly level does not count as being ahead",
   "Offside — any attacker positioned anywhere near the last defender when the ball is played forward should always be flagged offside regardless of their exact relative position",
   "A penalty kick, since a defender being that close to an onrushing striker is automatically considered a foul under the current laws of the game regardless of any actual contact",
   "A dropped ball, since offside decisions this close always require the referee to stop play immediately and restart with a drop ball rather than continuing play or awarding a free kick"
 ],
 "answer": 0,
 "explanation": "The offside law specifically requires the attacker to be nearer to the goal line than the second-last opponent — being exactly level is not offside. This precise, easily misunderstood detail is why 'level is onside' is one of the most commonly cited offside clarifications."
},
{
 "q": "During a match, the video assistant referee (VAR) reviews a goal and recommends the on-field referee check the pitchside monitor. After watching the replay, the referee disallows the goal for a clear handball in the buildup. What does this sequence illustrate about how VAR is actually meant to function?",
 "options": [
   "VAR supports the referee by flagging a 'clear and obvious error', but the final decision after reviewing the monitor still rests with the on-field referee, not with the VAR system automatically overturning the call itself",
   "VAR automatically overturns any decision it disagrees with, and the on-field referee has no remaining role or authority at all in the final decision once a VAR review has actually been triggered",
   "VAR is only used to check offside decisions specifically, so a handball review of this kind lies completely outside video assistant referee's actual defined scope of responsibility under the current laws",
   "VAR replaces the entire refereeing team for the remainder of the match once it has been used a single time, taking over full authority for every subsequent decision made for the rest of that match"
 ],
 "answer": 0,
 "explanation": "VAR is specifically designed to flag clear and obvious errors or missed serious incidents, but the on-field referee retains final decision-making authority, especially after a pitchside monitor review — VAR advises and highlights, it doesn't unilaterally overturn calls without the referee's own final judgement."
},
{
 "q": "A player takes a penalty kick, and just as their foot strikes the ball, the goalkeeper is standing with both feet clearly off the goal line, having stepped forward early. The kick is saved. What should happen next under the current laws?",
 "options": [
   "The penalty is retaken, since the goalkeeper must have at least part of one foot touching or in line with the goal line at the moment the kick is taken, and encroaching early is an infringement that voids a save",
   "The save stands and play continues normally, since goalkeepers are always permitted to move freely off their goal line at any time before or during a penalty kick with no restriction whatsoever",
   "The penalty taker is booked with a yellow card for taking the kick incorrectly, even though the actual infringement described was committed entirely by the goalkeeper rather than by the penalty taker",
   "The match is immediately abandoned, since any infringement occurring during a penalty kick specifically is treated as serious enough to require the referee to end the match altogether under current laws"
 ],
 "answer": 0,
 "explanation": "The goalkeeper must have at least part of one foot on or in line with the goal line at the moment the ball is kicked. A goalkeeper who has clearly moved off the line early and saves the kick has committed an infringement, and the standard remedy is a retake — a rule that exists specifically to prevent goalkeepers gaining an unfair advantage by encroaching."
},
{
 "q": "A defender, fully inside their own penalty area, deliberately handles the ball to stop it reaching an onrushing striker. The referee awards a penalty and shows the defender a red card for denying an obvious goalscoring opportunity. What combination of consequences does this scenario illustrate?",
 "options": [
   "A single infringement can trigger multiple simultaneous consequences — here, both a penalty kick award for the handball itself and a red card specifically for denying a clear goalscoring opportunity through that deliberate handling",
   "Only one consequence is ever permitted per single infringement under the laws of the game, so the referee in this scenario must choose between awarding either the penalty or the red card, but is never permitted to award both",
   "A deliberate handball inside the penalty area can never result in a red card under any circumstances, regardless of whether it also happens to deny an opponent an otherwise clear goalscoring opportunity",
   "The red card shown in this scenario must actually be for a completely separate, second offence, since deliberate handball alone is claimed to never be serious enough on its own to justify a sending-off of any kind"
 ],
 "answer": 0,
 "explanation": "A deliberate handball that denies an obvious goalscoring opportunity is treated as serious foul play, warranting both the penalty kick (for the handball offence itself) and a straight red card (for denying the goalscoring opportunity) — these are separate, cumulative consequences of the same single action, not alternatives to choose between."
},
{
 "q": "A striker is standing in an offside position when a teammate shoots at goal, but the ball deflects unpredictably off a defender before reaching the striker, who then scores. Assuming the striker didn't interfere with anyone before the deflection, what is the correct decision?",
 "options": [
   "The goal should stand — a deliberate play by a defender (not merely a deflection or save) resets the offside phase, since a genuinely deliberate action by a defender effectively means the striker's original starting position no longer applies",
   "The goal must always be disallowed for offside, since a player who was in an offside position at any earlier point during the passage of play is automatically deemed offside for the remainder of that phase, no matter what happens afterward",
   "The referee should stop play and restart with a dropped ball, since a deflection off a defender occurring after an offside position is held is treated identically to any other genuinely unclear or disputed refereeing situation",
   "The decision depends entirely and exclusively on which specific half of the pitch the deflection actually occurred in, since offside rules are officially applied completely differently between the two halves of the field of play"
 ],
 "answer": 0,
 "explanation": "The key distinction under the offside law is whether a defender's touch was a genuine, deliberate play of the ball (which resets the phase) versus merely a deflection or save (which does not) — a deliberate defensive action generally means a previously offside attacker is no longer penalised for their earlier position, since the phase of play has effectively restarted."
},
{
 "q": "A team is awarded a direct free kick just outside the opposition's penalty area. The referee paces out and enforces a minimum distance the defending wall must stand from the ball before the kick is taken. What is this minimum required distance?",
 "options": [
   "9.15 metres (10 yards) — the standard minimum distance opponents must retreat for any free kick, unless the free kick is taken quickly before the wall has a chance to retreat that full distance",
   "1 metre — a very short minimum distance that would make it essentially impossible for any defending wall to meaningfully block a direct shot at goal from a free kick taken this close to the penalty area",
   "There is no minimum required distance at all specified anywhere in the laws of the game, meaning defenders are legally permitted to stand directly on top of the ball itself if they choose to do so",
   "50 metres — a distance so large that it would push any defending wall entirely off the actual playing field for a free kick taken from just outside the edge of the penalty area in this specific scenario"
 ],
 "answer": 0,
 "explanation": "The standard minimum distance for a defending wall (or any opponent) at a free kick is 9.15 metres, equivalent to 10 yards — a distance referees are responsible for enforcing, using it to pace out and mark the appropriate spot before the kick is taken, unless the team taking the kick chooses to play it quickly before the wall retreats."
},
{
 "q": "A goalkeeper picks up a ball with their hands after a teammate deliberately kicks it back to them from open play. What is the correct decision?",
 "options": [
   "An indirect free kick is awarded to the opposing team from the spot where the goalkeeper handled the ball, since deliberately handling a teammate's deliberate back-pass is specifically prohibited under the laws of the game",
   "Nothing happens at all and play simply continues completely normally, since goalkeepers are permitted to use their hands on absolutely any ball played to them by a teammate under any circumstances whatsoever",
   "A penalty kick is awarded automatically to the opposing team regardless of exactly where on the pitch the goalkeeper actually handled the ball, since handling a deliberate back-pass is treated identically to any penalty-area handball",
   "The goalkeeper is shown a straight red card and sent off immediately, since handling a deliberate back-pass from a teammate is treated as serious foul play requiring an automatic dismissal under current laws"
 ],
 "answer": 0,
 "explanation": "The back-pass rule specifically prohibits a goalkeeper from handling the ball when it's been deliberately kicked to them by a teammate — the correct restart is an indirect free kick to the opposing team from where the handling occurred, a rule introduced specifically to prevent time-wasting through repeated back-passing to the keeper."
},
{
 "q": "Two players from opposing teams challenge for a loose ball. One player's studs-up sliding tackle makes forceful contact with the opponent's shin well before touching the ball at all, and the referee judges the challenge to have endangered the opponent's safety. What is the correct disciplinary outcome?",
 "options": [
   "A red card for serious foul play — using excessive force or endangering an opponent's safety in a challenge is treated as serious foul play, warranting a sending-off rather than merely a caution",
   "A yellow card only, since any tackle that results in some actual contact with the ball being won at any point during the challenge is always automatically downgraded to a caution rather than a sending-off",
   "No card of any kind, since the referee's judgement about whether a player's safety was actually endangered during a specific challenge is considered entirely irrelevant to any disciplinary decision under current laws",
   "An immediate abandonment of the entire match, since a tackle judged serious enough to endanger a player's safety is treated as automatically requiring the referee to end the match altogether"
 ],
 "answer": 0,
 "explanation": "A tackle that uses excessive force or endangers an opponent's safety — like a forceful studs-up challenge making contact with the shin before the ball — meets the definition of serious foul play, which is a sending-off offence (straight red card), distinct from a reckless but less dangerous foul that would typically only warrant a caution."
},
{
 "q": "A team's captain approaches the referee to ask about the reasoning behind a decision, staying calm and respectful throughout the conversation. Later, a substitute on the bench shouts abuse at the referee from the sideline. How do the laws of the game generally distinguish between these two situations?",
 "options": [
   "Calm, respectful dialogue (typically only the captain) about a decision is generally tolerated, while dissent through word or action — including abusive language from anyone, including a substitute — is a cautionable or sendable offence depending on severity",
   "There is no meaningful distinction between these two situations under the laws of the game, and both the captain's calm question and the substitute's abusive shouting would always receive exactly identical disciplinary treatment",
   "Only players who are actually on the pitch at that moment can ever receive any disciplinary sanction of any kind, meaning a substitute sitting on the bench is entirely and completely exempt from any possible caution or dismissal",
   "The referee is required to immediately abandon the match the moment any player or substitute says anything at all to the officiating team, regardless of tone, content, or the specific manner in which it was actually said"
 ],
 "answer": 0,
 "explanation": "Modern refereeing practice (and the laws) generally tolerate calm, respectful engagement — often specifically from the captain — about a decision, while dissent (abusive language, aggressive gestures) is a cautionable or, in serious cases, sendable offence, applicable to anyone involved in the match including substitutes on the bench, not just players actively on the pitch."
},
{
 "q": "A match is goalless after 90 minutes of normal time in a knockout cup tie that must produce a winner on the day. The rules for this specific competition specify two additional 15-minute periods before any further tiebreaker. What are these additional periods called?",
 "options": [
   "Extra time — two further periods played after a drawn knockout match when a winner must be determined, typically followed by a penalty shootout if the scores remain level after extra time as well",
   "Stoppage time — the additional minutes added at the end of each half of normal time to compensate for time lost to substitutions, injuries, and other delays, which is a completely different concept from a knockout tiebreaker period",
   "A replay — an entirely separate additional match played on a different day, rather than two extra periods played immediately following the original 90 minutes on the same day as described in this specific scenario",
   "A friendly — an informal, non-competitive match with no formal result recorded at all, which does not match the description of a competitive knockout cup tie that specifically requires an official winner to be determined"
 ],
 "answer": 0,
 "explanation": "Extra time refers to the two additional 15-minute periods played when a knockout match must produce a winner and normal time ends level — if the score remains tied after extra time as well, the match typically proceeds to a penalty shootout, a distinct concept from stoppage time (added within normal time) or a replay (an entirely separate rescheduled match)."
},
{
 "q": "An attacking player is fouled just outside the penalty area, and the referee plays advantage, waving play on because the attacking team retains a promising position with the ball. A few seconds later, the promising attack breaks down. What can the referee do at this point?",
 "options": [
   "The referee can still retrospectively penalise the original foul (typically within a few seconds) if the anticipated advantage doesn't actually develop, going back to award the free kick for the original offence",
   "Nothing further can be done at all once advantage has been played and signalled, since playing advantage is defined as an entirely final, permanently irreversible decision with absolutely no possibility of any later correction",
   "The referee must immediately abandon the match entirely, since any advantage that fails to actually develop as anticipated is treated as a serious refereeing error serious enough to require ending the match altogether",
   "The referee is required to award a penalty kick automatically regardless of the fact that the original foul actually occurred outside the penalty area rather than inside it, purely because the anticipated advantage failed to develop"
 ],
 "answer": 0,
 "explanation": "Playing advantage isn't an irreversible commitment — if the anticipated advantage doesn't actually materialise within a short window (typically a few seconds), the referee can still go back and penalise the original foul, giving the fouled team the free kick they would have received had advantage not initially been played."
},
{
 "q": "A defender clears the ball off their own goal line just before it fully crosses into the goal, and TV replays later show the ball's entire circumference was still marginally short of the goal line at the moment of clearance. What is the correct decision, and what technology exists specifically to help make this exact judgement accurately?",
 "options": [
   "No goal — the ball must fully cross the entire goal line to count as a goal, and goal-line technology exists specifically to make this exact, often extremely close judgement with far greater precision than the human eye alone can reliably achieve",
   "A goal should always be awarded in any situation this close, since any clearance attempt made directly on or extremely near the goal line is treated as sufficiently close to a goal to be awarded one regardless of the ball's exact actual position",
   "The decision is left entirely to a coin toss between the two team captains, since the laws of the game officially specify no other method whatsoever for resolving a goal-line decision this genuinely close and difficult to judge",
   "VAR is completely and entirely irrelevant to this specific type of decision, and goal-line technology has never actually been introduced or used in any professional match played anywhere in the world to date"
 ],
 "answer": 0,
 "explanation": "The law is unambiguous: the whole of the ball must cross the whole of the goal line for a goal to be given. Goal-line technology (a genuinely deployed system in many major competitions) exists specifically to resolve exactly this kind of extremely close, otherwise hard-to-judge call with far more precision and speed than a human official's eye alone."
},
{
 "q": "A substitute warming up on the touchline steps onto the field of play without the referee's permission and briefly interferes with an active passage of play before the referee notices and stops the game. What is the correct restart?",
 "options": [
   "An indirect free kick to the opposing team from the position where the interference actually occurred, since an unauthorised person (including an improperly entering substitute) interfering with play is treated as an outside-agent infringement",
   "The goal is automatically awarded to whichever team the interfering substitute belongs to, regardless of what was actually happening in that specific passage of play at the moment the substitute entered the field",
   "The match is immediately abandoned in every single case of this kind, since any unauthorised person entering the field of play during active play is always treated as serious enough to require ending the match altogether",
   "Play simply continues with no stoppage or restart of any kind at all, since a substitute standing on the touchline is considered to already be a fully authorised, legitimate part of play at all times during a match"
 ],
 "answer": 0,
 "explanation": "A substitute who enters the field without the referee's permission and interferes with play is treated as an outside agent — the restart is an indirect free kick for the opposing team from where the interference occurred, the standard remedy the laws provide for this category of infringement."
},
{
 "q": "A player is shown a yellow card for a reckless tackle, and later in the same match commits a second cautionable offence. What is the correct disciplinary outcome?",
 "options": [
   "A second yellow card in the same match results in a red card (effectively a sending-off via two cautions) and the player must leave the field for the remainder of the match",
   "Nothing additional happens beyond showing the second yellow card itself, since only a single card of any kind can ever actually be shown to any individual player during the entire course of one single match",
   "The second cautionable offence is automatically upgraded to a straight red card offence in every case, regardless of what the actual specific nature of that second offence itself happens to be",
   "The player is required to leave the field only temporarily for ten minutes, after which they are automatically permitted to return to play for the remainder of the match with no further restriction of any kind"
 ],
 "answer": 0,
 "explanation": "Two yellow cards shown to the same player in the same match result in a red card and dismissal — this is the standard 'second yellow' sending-off, distinct from a single straight red shown for a more serious first offence, but with the same practical outcome: the player leaves the field and the team continues with one fewer player."
},
{
 "q": "A corner kick is awarded, and as the ball is being placed, an attacking player deliberately encroaches inside the penalty area before the kick is taken, gaining a positional advantage. What is most consistent with how referees are generally expected to manage this kind of minor procedural infringement?",
 "options": [
   "Referees generally use game management and a warning for minor encroachment first, reserving a formal sanction for cases where the infringement is deliberate, repeated, or actually affects the outcome of the passage of play",
   "The referee is required to immediately abandon the entire match the very first time any player of any kind encroaches into the penalty area even slightly early before any set-piece kick is actually taken",
   "The corner kick is automatically cancelled and awarded to the opposing team as a goal kick instead, regardless of how minor or inconsequential the specific encroachment infringement actually was in this particular instance",
   "No response of any kind from the referee is ever appropriate in this situation, since minor positional encroachment before a corner kick is claimed to never actually be considered any kind of infringement under the current laws of the game"
 ],
 "answer": 0,
 "explanation": "In practice, referees generally exercise proportionate game management for minor, non-consequential procedural encroachment — a quiet word or brief delay to correct positioning — reserving a more formal sanction for cases that are deliberate, repeated, or that actually affect the fairness of the passage of play, rather than stopping the match for every small infringement."
},
{
 "q": "A goalkeeper claims and holds a football cleanly inside their own penalty area with both hands, and an opposing attacker continues to challenge physically for the ball after the goalkeeper has already gained clear control. What is the correct decision?",
 "options": [
   "A foul against the attacker for challenging a goalkeeper who has already gained clear control of the ball, since continuing to physically contest for the ball once a goalkeeper has secured possession is an infringement",
   "Nothing happens and play continues completely normally, since attackers are permitted to physically challenge a goalkeeper for the ball at any time regardless of whether that goalkeeper has already gained clear possession or not",
   "A goal kick is awarded automatically to the defending team purely because the goalkeeper happened to catch the ball cleanly, regardless of whatever the attacking player actually did or didn't do immediately afterward",
   "The attacking player is shown a straight red card automatically and immediately, since any physical challenge against a goalkeeper who has already secured the ball is always treated as serious enough to warrant a sending-off"
 ],
 "answer": 0,
 "explanation": "Once a goalkeeper has gained clear control of the ball with their hands inside their own penalty area, continuing to challenge them for it is a foul — this protection exists specifically to prevent dangerous, unnecessary physical contests for a ball that's already been legitimately secured."
},
{
 "q": "A referee allows a match to continue play for an additional 4 minutes beyond the initial 90, announced via the fourth official's board at the end of the second half, to compensate for substitutions, goal celebrations, and injury treatment that consumed time during the half. What is this additional time officially called?",
 "options": [
   "Stoppage time (also called injury time or added time) — extra minutes added at the end of a half specifically to compensate for time genuinely lost to stoppages during that half, distinct from extra time played after a drawn knockout match",
   "Extra time — the two additional 15-minute periods played specifically after a drawn knockout match that requires a winner on the day, which is a fundamentally different and much longer concept from a few added minutes within one half",
   "A penalty shootout — a method used to determine a winner after a match remains level, an entirely separate concept from any additional minutes played within the normal 90-minute duration of a single half of a match",
   "A replay — an entirely separate additional match rescheduled and played on a different day, which is completely unrelated to any additional minutes played at the end of an original match's normal 90-minute duration"
 ],
 "answer": 0,
 "explanation": "Stoppage time (injury time or added time) compensates for time genuinely lost during a half to substitutions, injuries, goal celebrations, and other delays — a fundamentally different, much shorter concept from extra time (two full additional periods played specifically after a drawn knockout match)."
},
{
 "q": "A striker, running onto a through ball, is fouled by a defender inside the penalty area, and the referee immediately points to the penalty spot. What is the correct procedure for taking this penalty kick?",
 "options": [
   "The ball is placed on the penalty spot, all players except the kicker and the goalkeeper must remain outside the penalty area and the penalty arc until the kick is actually taken, and the goalkeeper must stay on the goal line",
   "Any player from the fouled team is permitted to stand anywhere at all inside the penalty area, including directly next to the penalty spot itself, while the kick is actually being taken by the designated penalty taker",
   "The goalkeeper is required to stand at least five metres away from the actual goal line itself at the moment the penalty kick is taken, rather than remaining on the goal line as would normally be required",
   "The penalty kick must always be taken by whichever specific player was actually fouled in the penalty area, with no other teammate ever permitted to take the kick instead under any circumstances whatsoever"
 ],
 "answer": 0,
 "explanation": "Penalty kick procedure requires the ball on the penalty spot, all players other than the kicker and goalkeeper outside the penalty area and the penalty arc, and the goalkeeper remaining on the goal line until the ball is kicked — and critically, any eligible teammate (not necessarily the player who was fouled) may take the kick."
},
{
 "q": "During a match, a ball boy retrieves the ball quickly and hands it to a player taking a throw-in near the touchline, deliberately speeding up the restart to help the team currently trailing in the score. What does this scenario illustrate about the role of ball boys/girls under the spirit of fair officiating?",
 "options": [
   "Ball retrieval assistance is expected to be applied neutrally to both teams, and a match official noticing a pattern of favouritism (deliberately speeding up one team's restarts more than the other's) may intervene to ensure fairness",
   "Ball boys and girls have full, independent legal authority to make actual refereeing decisions during a match, meaning their choice to speed up one specific team's restart is treated as an official, formally binding decision",
   "This kind of scenario has no bearing whatsoever on fairness in a match, since who retrieves and returns the ball for a routine restart is considered entirely irrelevant to any aspect of a match's actual overall competitive fairness",
   "The team benefiting from this kind of favourable ball-boy treatment must be immediately and automatically disqualified from the match entirely, regardless of whether the assistance itself actually had any real effect on the final result"
 ],
 "answer": 0,
 "explanation": "While ball boys/girls aren't official match officials, the expectation of fair, neutral administration of a match extends to practical matters like ball retrieval — a match official noticing a clear pattern of one-sided favouritism (which has been a real, documented talking point in professional football) may reasonably intervene to preserve the fairness of the contest."
},
{
 "q": "A player receives the ball with their back to goal, in an offside position, but immediately passes it backward to an onside teammate without ever touching, playing, or interfering with an opponent or challenging for the ball themselves. What is the correct decision regarding the player's earlier offside position?",
 "options": [
   "Merely being in an offside position is not itself an offence — a player is only penalised for offside if they become actively involved in play by interfering with an opponent, interfering with play, or gaining an advantage from that position",
   "The player should always be penalised for offside automatically the instant they are found to be standing in an offside position, regardless of whether they ever actually touch the ball, interfere with an opponent, or become involved in play in any way",
   "The referee must abandon the passage of play immediately and restart with a dropped ball, since any offside position at all, even one where the player never becomes actively involved, is treated as requiring an immediate stoppage",
   "A yellow card must always be shown automatically to any player found standing in an offside position, regardless of what that player subsequently actually does or doesn't do with the ball once they receive it"
 ],
 "answer": 0,
 "explanation": "This is a frequently misunderstood detail: simply standing in an offside position isn't an offence by itself — a player is only penalised if they become actively involved in play from that position, by interfering with an opponent, interfering with play, or gaining an advantage. A player who receives the ball and immediately passes it away without any of that hasn't committed an offside offence."
},
{
 "q": "A team's goalkeeper is injured with no substitutes remaining on the bench, forcing an outfield player to put on the goalkeeper jersey and finish the match in goal. What does this scenario illustrate about substitution rules?",
 "options": [
   "Once a team has used all its permitted substitutions, it must continue with the players remaining on the pitch even in the event of a further injury, which is exactly why an outfield player sometimes has to fill in as emergency goalkeeper",
   "Teams are always permitted unlimited substitutions specifically in the event of a genuine goalkeeper injury, regardless of how many substitutions that same team has already used earlier in the same match for any other reason",
   "The match must be immediately abandoned the moment any team's goalkeeper is injured with no remaining substitutes available on the bench, since playing without a recognised specialist goalkeeper is not permitted under current laws",
   "The opposing team is automatically awarded the match as an official win by forfeit whenever any team is forced to field an outfield player in goal due to having exhausted all of their permitted substitutions"
 ],
 "answer": 0,
 "explanation": "Once a team has used all permitted substitutions, it must continue with the players it has on the field even if another injury (including to the goalkeeper) occurs — exactly the situation that leads to the memorable, occasionally seen scenario of an outfield player pulling on the goalkeeper jersey and finishing out a match in goal."
},
{
 "q": "A player deliberately kicks the ball out of play to allow an injured opponent to receive treatment, and by common convention, the opposing team throws the ball back to the team that originally kicked it out once play resumes. What does this practice illustrate about football's culture beyond the formal written laws?",
 "options": [
   "Football has informal sporting conventions, respected by players even though they aren't strictly written into the laws of the game, reflecting a broader culture of fair play alongside the formal rulebook",
   "This convention is actually a formally written, mandatory law of the game, meaning any team that fails to return the ball this way after an opponent's injury stoppage can be formally sanctioned by the referee",
   "This practice has no genuine real-world basis and does not actually occur in any real professional match, making this entire described scenario a purely hypothetical, invented example with no connection to how football is actually played",
   "The convention exists specifically and exclusively to slow the match down deliberately, with genuinely no connection whatsoever to any player's actual well-being, safety, or need for legitimate injury treatment"
 ],
 "answer": 0,
 "explanation": "Returning the ball after an opponent kicked it out for an injury is a widely respected sporting convention, not a formally written law — its existence and general observance reflects football's broader informal culture of fair play operating alongside, and sometimes going beyond, the strictly written rulebook."
},
{
 "q": "A defender slides in to block a shot and the ball strikes their raised arm, which was held in a position clearly away from their body in a way that made their overall body shape unnaturally larger, even though the defender argues they didn't intend to handle the ball deliberately. How does modern handball interpretation generally treat this situation?",
 "options": [
   "An arm in an unnaturally raised or extended position that makes the body unnaturally bigger can be judged a handball offence even without clear deliberate intent, since current interpretation weighs arm position and resulting body silhouette, not just conscious intent",
   "No offence can ever occur under any circumstances unless the referee can somehow directly read and confirm the defender's actual internal, subjective intent to deliberately handle the ball at the exact moment of contact",
   "Handball can only ever be judged an offence if the defender's hand or arm is the very first part of their entire body to make contact with the ball, regardless of that specific arm's actual position at the moment of contact",
   "This situation can never realistically occur in any actual professional match, since defenders sliding to block a shot are claimed to never have their arms positioned anywhere near the path of the ball in any real scenario"
 ],
 "answer": 0,
 "explanation": "Modern handball interpretation moved away from requiring clear, provable deliberate intent as the sole test — an arm held in an unnatural position that makes the body's silhouette bigger can be judged an offence based on that positioning itself, which is exactly why 'unintentional' handballs involving an unnaturally raised arm are still frequently penalised."
},
{
 "q": "A team is defending a one-goal lead deep into stoppage time, and a player deliberately and repeatedly takes an unnecessarily long time to retrieve the ball and take a routine throw-in, ignoring the referee's request to speed up. What is the referee entitled to do in response to this specific behaviour?",
 "options": [
   "Caution the player with a yellow card for delaying the restart of play, a recognised cautionable offence specifically covering exactly this kind of deliberate time-wasting behaviour",
   "Nothing at all can be done by the referee in this specific situation, since deliberately delaying a routine throw-in restart is claimed to never actually be considered any kind of disciplinary offence under the current laws of the game",
   "The referee must immediately award the opposing team an automatic goal, since delaying a throw-in restart late in a match is treated as serious enough on its own to warrant an automatic goal being awarded to the opposition",
   "The match must be immediately abandoned altogether, since any deliberate delay of a restart of play by any player is treated as serious enough on its own to require the referee to end the entire match"
 ],
 "answer": 0,
 "explanation": "Delaying the restart of play is a specifically recognised cautionable offence — a yellow card is the standard, proportionate sanction for exactly this kind of deliberate time-wasting behaviour late in a match, giving the referee a clear tool to discourage and penalise it without needing to resort to anything more severe."
},
{
 "q": "A referee shows a player a yellow card for a foul, then a few minutes later shows the same player a second yellow card for a completely separate, unrelated offence, followed immediately by a red card. How many total cards were shown to this one player, and why?",
 "options": [
   "Three cards were shown in total — two separate yellow cards for two separate offences, with the second yellow automatically triggering the red card and resulting dismissal, all three of which are typically recorded in the match report",
   "Only one single card was actually shown in total, since a second yellow card and its resulting automatic red card are always recorded and counted together as a single, combined disciplinary event rather than as separate cards",
   "No card was actually shown to the player at all in this scenario, since a second yellow card automatically and immediately cancels out the disciplinary weight of the earlier first yellow card that had already been shown",
   "Exactly four separate cards were shown in this specific scenario, since the laws of the game are claimed to require the referee to show an additional card specifically to the player's own team captain as well"
 ],
 "answer": 0,
 "explanation": "The sequence is: first yellow card for offence one, second yellow card for offence two, and then the red card shown immediately after to confirm the resulting dismissal — three separate cards shown in total, all of which are typically recorded distinctly in the official match report, even though the practical outcome is one sending-off."
},
{
 "q": "A goal kick is taken, and the ball must clear the penalty area before any other player (from either team) is allowed to touch it. A defending player touches the ball while it's still inside the penalty area, before it has left. What is the correct restart?",
 "options": [
   "The goal kick is retaken, since the ball must leave the penalty area before being touched by any other player, and a touch before that point means the original goal kick has not been properly and legally completed",
   "The opposing team is awarded a direct free kick from the exact spot where the ball was actually touched, treating this specific situation identically to how a normal, standard in-play foul would be treated",
   "Nothing at all happens and play simply continues completely normally, since the requirement for a goal kick to fully leave the penalty area before being touched by anyone else is claimed not to actually exist under current laws",
   "The opposing team is awarded a corner kick instead, treating this specific situation as though the original goal kick attempt had somehow gone out of play over the defending team's own goal line entirely"
 ],
 "answer": 0,
 "explanation": "A goal kick isn't properly in play until the ball has left the penalty area — if any player touches it before that happens, the kick is retaken, a rule that exists to ensure the goal kick is genuinely completed as a restart before normal play (and second touches from either team) resumes."
},
{
 "q": "A team's kit includes shin guards covered entirely by the players' socks, as required by law, but one player is discovered at half-time to have not been wearing shin guards at all during the entire first half. What is the correct handling of this situation once discovered?",
 "options": [
   "The player must not be permitted to participate further without correcting the equipment issue, since shin guards are mandatory required equipment under the laws of the game, and this is generally addressed as soon as it's actually discovered",
   "Nothing needs to happen at all in response to this discovery, since shin guards are claimed to be an entirely optional piece of equipment that no player is actually required to wear under the current laws of the game",
   "The entire first half must be immediately replayed in full from the very beginning, since any player found to have been missing mandatory equipment invalidates every single result and event from that entire first half of play",
   "The player is issued an automatic straight red card retroactively for the offence, and their entire team is immediately disqualified from the whole competition, purely for this specific mandatory equipment violation"
 ],
 "answer": 0,
 "explanation": "Shin guards are mandatory required equipment under the laws of the game — a player discovered without them (however that's caught, commonly at half-time or during a check) generally can't continue without correcting the issue, though the earlier play itself typically isn't retroactively invalidated once discovered after the fact."
},
{
 "q": "A player is fouled just outside the penalty area, and their team is awarded a direct free kick in a promising, shooting position. The kicker curls the ball directly into the goal without any other player touching it. What type of free kick allows a goal to be scored directly like this, and how does that differ from the alternative?",
 "options": [
   "This is a direct free kick — a goal can be scored straight from the kick without needing to touch another player first, unlike an indirect free kick, which requires the ball to touch a second player (from either team) before a goal can count",
   "This is an indirect free kick, and the goal should actually be disallowed, since an indirect free kick specifically requires the ball to touch a second player before a goal is legally permitted to be scored directly from that kick",
   "There is no meaningful difference at all between a direct free kick and an indirect free kick under the current laws of the game, and both kick types are always treated in every possible respect completely identically",
   "The type of free kick awarded in any given situation is determined entirely and exclusively by which specific half of the pitch the original foul actually occurred in, rather than by the actual specific nature of the foul itself"
 ],
 "answer": 0,
 "explanation": "A direct free kick can result in a goal scored straight from the kick itself, with no need for any other touch — this is distinct from an indirect free kick (signalled by the referee raising an arm), which specifically requires the ball to touch a second player, from either team, before a goal can legally be awarded."
},
{
 "q": "A referee cautions a player for a reckless challenge, then a teammate of the fouled player confronts the fouling player aggressively, shoving them in apparent retaliation. What is the most consistent way for the referee to handle both incidents?",
 "options": [
   "Each incident is assessed and sanctioned separately on its own individual merits — the original reckless challenge and the retaliatory shove are two distinct offences, each potentially warranting its own separate caution or more serious sanction",
   "Only the very first incident (the original reckless challenge) can ever actually be sanctioned in this kind of scenario, since any retaliatory action that happens afterward is claimed to always be considered automatically and fully justified",
   "Both incidents must always be cancelled out against each other and treated as though absolutely nothing at all had actually happened, since two separate offences occurring in quick succession are claimed to always fully offset one another",
   "The referee is required to immediately abandon the entire match the moment more than one single disciplinary incident of any kind occurs within the same short passage of play during any part of the match"
 ],
 "answer": 0,
 "explanation": "Referees generally assess and sanction each incident separately based on its own actual merits — the original reckless challenge and a subsequent retaliatory shove are two distinct offences, each potentially warranting its own caution or more serious sanction, rather than one incident being excused or cancelled out simply because it followed another."
},
{
 "q": "A defender fouls the last attacker just outside the penalty area, clearly denying an obvious goalscoring opportunity, even though no penalty is awarded since the foul happened outside the box. What is the correct disciplinary outcome for the defender?",
 "options": [
   "A red card for denying an obvious goalscoring opportunity — this offence can apply to a foul committed anywhere on the pitch, not only inside the penalty area, since the key factor is denying a clear goalscoring chance, not the foul's exact location",
   "Only a yellow card can ever be shown in this situation, since a red card for denying an obvious goalscoring opportunity is claimed to apply exclusively to fouls committed by a defender specifically inside their own penalty area",
   "No card of any kind is shown in this specific situation, since a foul that occurs outside the penalty area is treated as automatically exempt from any possible red-card sanction under the current laws of the game",
   "The referee must award a penalty kick regardless of where the foul actually occurred, purely because it denied an obvious goalscoring opportunity, overriding the normal requirement that a penalty only follows a foul actually committed inside the box"
 ],
 "answer": 0,
 "explanation": "Denying an obvious goalscoring opportunity through a foul is a sending-off offence regardless of whether the foul happens inside or outside the penalty area — inside the box it's typically paired with a penalty kick, but outside the box (where no penalty applies) the red card for denying the goalscoring opportunity still stands on its own."
},
{
 "q": "A player performs a throw-in but lifts one foot off the ground during the throwing motion, and the ball is delivered using only one hand rather than both. What is the correct decision?",
 "options": [
   "A foul throw — proper technique requires both feet to remain on the ground (on or behind the touchline) and the ball to be delivered with both hands from behind and over the head, so this throw is an infringement awarded as a throw-in to the other team",
   "The throw-in is perfectly legal and play continues completely normally, since the laws of the game are claimed to place no actual restriction whatsoever on foot placement or hand usage during any throw-in technique",
   "A yellow card is shown automatically to the player for the infringement, since an improperly taken throw-in of this kind is treated as a cautionable offence under current laws rather than simply as a foul throw",
   "The referee awards a penalty kick to the opposing team, treating this specific improper throw-in technique identically to how a genuine penalty-area foul would normally be treated under the laws of the game"
 ],
 "answer": 0,
 "explanation": "A legal throw-in requires both feet on the ground (on or behind the touchline) and delivery with both hands from behind and over the head — violating either requirement (lifting a foot, using only one hand) is a foul throw, with the restart simply being a throw-in awarded to the other team, not a card or a penalty."
},
{
 "q": "A referee blows the half-time whistle, and the two teams are given a break before the second half begins. What is the maximum duration the laws of the game specify for this interval, unless the competition rules state otherwise?",
 "options": [
   "15 minutes — the standard maximum half-time interval, though it may be shortened by mutual agreement or specific competition rules, but not extended beyond this without special permission from the relevant authority",
   "60 minutes — a duration long enough that it would functionally make a scheduled match nearly twice as long overall, which does not match how half-time intervals are actually specified or generally applied in professional football",
   "There is no maximum duration specified anywhere in the laws of the game at all, meaning a half-time interval could technically be extended indefinitely at either team's or either coach's sole individual discretion",
   "5 seconds — a duration so brief that it would not realistically allow players any meaningful time at all to leave the pitch, receive any tactical instruction, or take even a short rest before the second half begins"
 ],
 "answer": 0,
 "explanation": "The laws specify a maximum 15-minute half-time interval unless competition rules state otherwise — a defined limit that exists specifically to keep the overall match length and broadcast/spectator experience reasonably predictable and consistent, while still giving players a genuine rest and tactical reset."
},
{
 "q": "During a match, a sudden severe thunderstorm makes conditions genuinely dangerous for players on an open pitch. What authority does the referee have in this situation?",
 "options": [
   "The referee has the authority to suspend or abandon the match due to genuinely dangerous conditions like severe weather, since player safety is a fundamental refereeing responsibility that overrides simply completing the fixture as scheduled",
   "The referee has no authority whatsoever to stop a match for any weather-related reason under any circumstances, and is required to continue play regardless of how genuinely dangerous the actual conditions on the pitch have become",
   "Only a senior competition official physically present in the stadium's administrative office, and never the actual on-field referee themselves, is ever permitted to make any decision at all about stopping a match for dangerous weather",
   "The decision to stop a match for dangerous weather conditions can only ever be made by a formal vote among both team captains, with the referee having no independent decision-making authority of their own in this specific situation"
 ],
 "answer": 0,
 "explanation": "The referee has genuine authority to suspend or abandon a match when conditions become dangerous, including severe weather like a thunderstorm with lightning risk — player safety is treated as a fundamental refereeing responsibility, taking priority over simply completing a scheduled fixture on time."
},
{
 "q": "Play is stopped because the ball accidentally strikes the referee and deflects to an attacking player in a promising position, with no clear possession established at the moment of the stoppage. What is the correct method of restarting play?",
 "options": [
   "A dropped ball — used to restart play fairly after a stoppage where possession wasn't clearly with one team (like the ball deflecting unpredictably off the referee), contested between two players, one from each team",
   "A direct free kick is awarded automatically to whichever team the ball happened to deflect toward, treating an accidental deflection off the referee identically to how an actual, deliberate foul committed by a player would be treated",
   "The match is immediately abandoned entirely, since the ball accidentally striking the match officials themselves is treated as serious enough on its own to require ending the entire match under current laws",
   "A penalty kick is awarded automatically to the defending team in this scenario, regardless of where on the actual pitch the deflection off the referee happened to occur relative to either team's own goal"
 ],
 "answer": 0,
 "explanation": "A dropped ball is the standard restart used when play must resume after a stoppage without a clear foul or clear possession — the ball deflecting unpredictably off the referee is exactly this kind of situation, restarted fairly by dropping the ball for a contest between two players rather than awarding a free kick or penalty to either side."
},
{
 "q": "A team's manager is confined to a marked technical area beside the pitch during a match but repeatedly steps outside its boundary to shout tactical instructions closer to the field, ignoring the fourth official's requests to return. What can happen as a result of this repeated behaviour?",
 "options": [
   "The manager can be cautioned or, for persistent or serious misconduct, dismissed from the technical area and sent to the stands, since managing behaviour within the technical area is part of the match officials' overall disciplinary responsibility",
   "Nothing at all can happen in this situation, since technical area boundaries are claimed to be purely a matter of informal broadcast convention with no actual, formal disciplinary weight whatsoever attached to them",
   "The manager's entire team is immediately and automatically disqualified from the whole match purely as a result of the manager's own repeated personal behaviour, regardless of anything the players on the pitch are actually doing",
   "The referee is required to immediately abandon the match altogether the very first time any coach or manager steps outside their own designated technical area boundary at any point during a match"
 ],
 "answer": 0,
 "explanation": "The technical area has real, formal disciplinary weight — a manager who persistently oversteps its boundary or ignores official requests can be cautioned or, for serious or repeated misconduct, dismissed to the stands, since managing the touchline environment is genuinely part of match officials' broader disciplinary responsibility."
},
{
 "q": "A player is shown a yellow card in the 89th minute of a match for a reckless challenge, and immediately afterward, while still visibly angry, kicks the ball away in protest and shouts abuse at the referee. What is the most likely correct outcome?",
 "options": [
   "A second caution (yellow card) for dissent, which combined with the earlier yellow becomes a second-yellow red card and dismissal, since kicking the ball away and shouting abuse are each separately cautionable offences",
   "Nothing further happens beyond the original yellow card already shown, since any misconduct occurring immediately after a card has just been shown is claimed to always be considered part of that same single original offence",
   "The referee is required to immediately abandon the match entirely, since dissent shown by a player who has already received one yellow card earlier in the same match is treated as serious enough to end the match",
   "The match continues with absolutely no further action of any kind at all, since dissent and kicking the ball away are claimed to never actually be considered cautionable offences under the laws of the game"
 ],
 "answer": 0,
 "explanation": "Kicking the ball away in protest and abusive dissent toward the referee are each separately recognised cautionable offences — combined with the earlier yellow card already shown, a second caution here would trigger the second-yellow red card and dismissal, illustrating how misconduct after a decision can escalate a player's own disciplinary situation."
},
{
 "q": "A player is judged by the referee to have dived inside the penalty area, exaggerating or simulating contact from a defender to try to win a penalty kick that wasn't actually deserved. What is the correct disciplinary response?",
 "options": [
   "A caution (yellow card) for unsporting behaviour, since attempting to deceive the referee by simulating a foul is specifically treated as a cautionable offence under the laws of the game, alongside no penalty being awarded",
   "A penalty kick is still awarded to the diving player's own team regardless of the referee's own genuine judgement that no actual foul occurred, purely because the attacking player is the one who went down inside the box",
   "The referee is required to immediately abandon the entire match the moment any single act of simulation is identified by that referee anywhere on the pitch, regardless of that specific incident's severity",
   "No response of any kind is appropriate or required, since simulation to win a penalty is claimed to never actually be treated as any kind of cautionable offence under the current laws of the game"
 ],
 "answer": 0,
 "explanation": "Simulation (diving) to deceive the referee, including to win a penalty that wasn't deserved, is a specifically recognised cautionable offence under unsporting behaviour — the correct outcome is no penalty awarded, plus a yellow card for the attempted deception, not a penalty rewarded despite the referee's own genuine judgement."
},
{
 "q": "A scuffle breaks out involving several players from both teams after a hard tackle, with players from the substitutes' bench also running onto the pitch to get involved. How do match officials generally approach identifying and sanctioning individual misconduct in this kind of mass confrontation?",
 "options": [
   "Officials (aided by assistant referees, the fourth official, and increasingly video review) attempt to identify specific individual actions — like throwing a punch versus merely being present — since blanket, undifferentiated sanctions for an entire group are not how individual disciplinary responsibility is generally assessed",
   "Every single player and substitute who was present anywhere near the confrontation, regardless of what they individually actually did, is automatically shown an identical red card with no distinction made between different individual actions",
   "The match is always immediately and completely abandoned the instant any confrontation involving more than two total players from both teams combined breaks out at any point during any match",
   "No disciplinary action of any kind is ever taken in this kind of situation, since mass confrontations involving many separate players are claimed to be considered too genuinely complicated for any referee to realistically sort out"
 ],
 "answer": 0,
 "explanation": "Modern officiating (often assisted by video review after the match, even where in-game VAR isn't used for this specific purpose) tries to distinguish individual actions within a mass confrontation — a player who threw a punch is treated very differently from one who was simply present or tried to act as peacemaker, rather than applying an identical blanket sanction to everyone involved."
},
{
 "q": "A match is played in extreme heat, and the referee calls a brief scheduled pause partway through each half specifically to allow players to hydrate, separate from the normal flow of stoppages for fouls or injuries. What is this kind of scheduled pause generally called?",
 "options": [
   "A cooling break (or water break) — a scheduled pause, used in extreme heat conditions, specifically to let players hydrate and briefly recover, distinct from stoppage time added for fouls, injuries, or substitutions",
   "Extra time — the two additional 15-minute periods played after a drawn knockout match requiring a winner, a completely different, much longer concept unrelated to a brief scheduled hydration pause during a single half",
   "A dropped ball — a specific method used to restart play fairly after a stoppage without clear possession, an entirely different concept unrelated to a scheduled pause specifically for player hydration in extreme heat",
   "A technical area — the marked space beside the pitch where coaches and substitutes are required to remain during a match, a completely different physical-space concept unrelated to any scheduled in-match hydration pause"
 ],
 "answer": 0,
 "explanation": "A cooling break (or water break) is a scheduled pause specifically introduced for extreme heat conditions, letting players hydrate and briefly recover mid-half — a distinct, deliberately scheduled concept from the normal flow of stoppages for fouls, injuries, or substitutions, and from stoppage time added at the end of a half."
},
{
 "q": "A player suffers a clear blow to the head during a collision and is showing visible signs of disorientation, but insists to the medical staff that they feel fine and want to continue playing. What is the generally accepted modern approach to this situation in football's concussion protocols?",
 "options": [
   "The player should be withdrawn from the match if genuine concussion is suspected, regardless of the player's own insistence they feel fine, since visible signs of disorientation are treated as a serious safety concern that overrides a player's own self-assessment",
   "The player's own personal insistence that they feel fine is treated as fully and completely decisive under modern concussion protocols, meaning medical staff have no independent authority to withdraw a player who states they want to continue",
   "Concussion protocols in football are claimed to not actually exist in any real, formal way, meaning this entire scenario represents a situation with no established medical or refereeing guidance of any kind currently in place",
   "The decision on whether to withdraw a potentially concussed player is left entirely and exclusively to that player's own manager or head coach, with genuinely no involvement whatsoever from any actual medical staff in this decision"
 ],
 "answer": 0,
 "explanation": "Modern concussion protocols in football specifically prioritise erring on the side of caution — visible signs of a potential concussion generally warrant withdrawing a player for further assessment regardless of that player's own insistence they feel fine, reflecting growing awareness of the serious, sometimes delayed risks of playing on with a head injury."
},
{
 "q": "Two teams turn up to a match wearing kits that are too similar in colour for players, officials, and spectators to reliably distinguish at a glance. What is the standard way this kind of kit clash is generally resolved before kickoff?",
 "options": [
   "One team (typically the designated away team, or as otherwise specified by competition rules) changes into an alternate kit that provides sufficient visual contrast, a resolution generally sorted out before the match rather than during it",
   "The match is immediately and automatically abandoned entirely the moment any kit colour clash of any kind is discovered, since a kit clash is treated as serious enough on its own to prevent any match from being played at all",
   "Nothing needs to be done at all in this situation, since kit colours are claimed to have no genuine practical bearing whatsoever on players', officials', or spectators' actual ability to follow and understand a match",
   "Both teams' entire playing squads are required to be replaced immediately with a completely different set of players wearing pre-approved kits, rather than simply having one specific team change into an alternate kit as usual"
 ],
 "answer": 0,
 "explanation": "A kit clash is a routine, practical problem generally resolved before kickoff, with the away team (or as otherwise specified by competition rules) typically switching to an alternate kit that provides sufficient visual contrast — an administrative matter handled proactively, not something that would ever cause a match to be abandoned."
},
{
 "q": "A team has three players sent off during a match, reducing their number of players on the pitch to six, and the laws specify a minimum number of players required for a match to continue. What happens if a team drops below that minimum?",
 "options": [
   "The match must be abandoned if a team's number of players falls below the minimum required (commonly seven, subject to specific competition rules), since a match cannot continue fairly or safely below that threshold",
   "The match continues completely normally with genuinely no limit whatsoever on how few players either team is actually permitted to field, all the way down to a single remaining player on the pitch if that were to occur",
   "The opposing team is automatically required to also reduce their own number of players down to match whatever reduced number the shorthanded team currently has, so that both sides always remain perfectly numerically equal",
   "The team that has had players sent off automatically wins the match by forfeit purely as a direct result of having players sent off, regardless of the actual score or any other circumstances of the match itself"
 ],
 "answer": 0,
 "explanation": "Competition rules commonly specify a minimum number of players (often seven) below which a match can no longer continue and must be abandoned — reflecting that below a certain threshold, a genuinely fair and safe contest between the two sides is no longer realistically possible, regardless of the specific reason for the reduction."
},
{
 "q": "A defender attempts to clear the ball but instead deflects it into their own net, with no attacking player having touched the ball at all during that particular passage of play. How is this goal officially recorded?",
 "options": [
   "As an own goal, credited to the defending team and counted against them on the scoreline, since the ball entered the net as a direct result of the defending player's own action rather than any attacking player's shot or touch",
   "The goal doesn't count at all and is disallowed entirely, since a goal is claimed to only ever be valid under the laws of the game if it was actually scored directly by an attacking player rather than by any defending player",
   "The goal is instead credited to whichever attacking player happened to be positioned physically closest to the ball at the specific moment it actually crossed the goal line, regardless of what that specific attacker actually did",
   "The referee is required to immediately abandon the match entirely, since a defending player accidentally scoring into their own team's own net is treated as serious enough on its own to require ending the match"
 ],
 "answer": 0,
 "explanation": "An own goal is a fully valid, counted goal — recorded against the defending team on the scoreline even though no attacking player touched the ball during that passage, since what matters for a goal is that the whole ball crossed the whole goal line, not specifically which team's player was responsible for putting it there."
},
{
 "q": "A corner kick is being set up, and the referee checks that the ball is properly placed within the quarter-circle marked at the corner of the pitch before allowing the kick to be taken. What is the purpose of this specific marking?",
 "options": [
   "It defines the exact area within which the ball must be placed for a corner kick to be legally taken, ensuring a consistent, fair, and clearly defined starting position for every corner kick regardless of which specific corner it's taken from",
   "It marks the exact spot where the goalkeeper is legally required to stand throughout the entire corner kick, which is a completely different purpose from any rule about where the actual ball itself must be placed",
   "It indicates the specific area where any potential offside decision related to that particular corner kick will always be determined, which is unrelated to the specific ball-placement purpose the quarter-circle actually serves",
   "It has no real practical or rules-based purpose whatsoever, and is claimed to exist purely as a cosmetic pitch-marking convention with no genuine bearing on how a corner kick is actually and legally taken"
 ],
 "answer": 0,
 "explanation": "The corner arc (quarter-circle) defines the precise area where the ball must be placed for a corner kick to be legally taken, ensuring a consistent, clearly defined, and fair starting position for the kick regardless of which of the pitch's four corners it happens to be taken from."
},
{
 "q": "The offside law specifically states that a player cannot be penalised for offside directly from a throw-in, a goal kick, or a corner kick, even if they would otherwise be in an offside position when the ball is played. What is the practical significance of this specific exception?",
 "options": [
   "It means an attacker can legitimately stand in what would normally be an offside position specifically when the ball is about to be restarted via one of these three specific set pieces, without being penalised, unlike during general open play",
   "It means these three restarts (throw-ins, goal kicks, corner kicks) are the only situations in the entire game where offside can actually ever be called, making offside inapplicable to every other normal open-play situation",
   "It means a team is never permitted to score directly from any of these three specific restarts under any circumstances, since offside exceptions are claimed to always come paired with an automatic prohibition on scoring",
   "It has no real practical significance of any kind at all, since this specific rule is claimed to never actually be relevant or applied in any real professional match played anywhere in the world"
 ],
 "answer": 0,
 "explanation": "This is a specific, deliberate exception: offside cannot be called directly from a throw-in, goal kick, or corner kick, meaning an attacker can legitimately occupy what would otherwise be an offside position specifically at that exact restart — a detail distinct from general open-play offside, where the same positioning would normally be penalised."
},
{
 "q": "A goalkeeper picks up the ball with their hands inside their own penalty area and, after a noticeable delay, is judged by the referee to be holding onto it for an excessively long time without releasing it back into play. What is the correct decision under the modern six-second guidance?",
 "options": [
   "An indirect free kick can be awarded to the opposing team if the goalkeeper is judged to have held the ball unreasonably long (guided by roughly six seconds) without releasing it, a rule specifically intended to prevent time-wasting",
   "Nothing at all happens in this situation regardless of how long the goalkeeper actually holds the ball, since goalkeepers are claimed to be permitted to hold the ball in their own hands for an unlimited amount of time with no restriction whatsoever",
   "A penalty kick is awarded automatically to the opposing team purely because the goalkeeper held the ball for what the referee judged to be an excessively long period, treating this specific delay identically to a genuine penalty-area foul",
   "The goalkeeper is shown a straight red card and sent off immediately, since holding the ball for an excessively long time is treated as serious foul play requiring an automatic sending-off under the current laws of the game"
 ],
 "answer": 0,
 "explanation": "The laws give referees the ability to penalise a goalkeeper who holds the ball unreasonably long without releasing it, with roughly six seconds commonly used as practical guidance — the correct sanction is an indirect free kick to the opposing team, a rule specifically aimed at preventing time-wasting through prolonged, unnecessary holding of the ball."
},
{
 "q": "A team captain wears a distinctive armband throughout a match, distinguishing them from their teammates. Beyond a general leadership role, what specific, formally recognised function does the captain generally have during a match according to common practice?",
 "options": [
   "The captain is often the primary or sole player expected to approach the referee respectfully to seek clarification on a decision, and may have specific ceremonial duties like the pre-match coin toss, though the armband itself confers no additional formal rule-based powers beyond this recognised role",
   "The captain has the formal legal authority to personally overrule any refereeing decision made during the match, meaning the referee is required to defer entirely to the captain's own judgement whenever a genuine disagreement occurs",
   "The captain is the only player on the entire team who is permitted to ever take a penalty kick, throw-in, or corner kick under any circumstances, with every other teammate being formally barred from taking any of these three restarts",
   "The captain's armband grants that specific player complete legal immunity from receiving any yellow or red card of any kind for the entire duration of any match in which they are wearing it, regardless of what that player actually does"
 ],
 "answer": 0,
 "explanation": "The captain has a recognised, if largely informal, role — commonly being the player expected to calmly approach the referee for clarification on a decision, and having specific ceremonial duties like the pre-match coin toss — but the armband confers no actual additional formal rule-based power, immunity, or exclusive restart-taking privilege under the laws of the game."
},
{
 "q": "A referee decides, based on genuine safety concerns after crowd trouble breaks out in the stands, to suspend a match indefinitely partway through the second half rather than allow it to continue. What is this outcome generally called, and how does it typically differ from a match that simply ends normally at full time?",
 "options": [
   "This is an abandoned match — ended before its natural conclusion due to a serious issue like safety concerns, weather, or insufficient players, which typically requires the relevant competition authority to separately decide how (or whether) the match is completed or replayed",
   "This is identical in every respect to a match ending normally at full time, with the final score at the exact moment of suspension always being immediately and permanently recorded as the match's official final result with no further authority review needed",
   "This is officially classified as extra time, the same two additional 15-minute periods played after a drawn knockout match requiring a winner, despite the fact that this scenario clearly describes a suspension rather than any additional period of play",
   "This is officially classified as a walkover, a result specifically awarded when one team fails to show up to play at all, which does not match this scenario where both teams were already actively playing before the suspension occurred"
 ],
 "answer": 0,
 "explanation": "An abandoned match ends before its natural conclusion due to a serious issue like crowd trouble, dangerous weather, or a team falling below the minimum player count — unlike a match completing normally at full time, an abandoned match typically requires the relevant competition authority to separately decide afterward how (replay, resume, or another outcome) the match should actually be resolved."
},
{
 "q": "A striker is clearly through on goal with only the goalkeeper to beat, and a covering defender, with no realistic chance of playing the ball itself, deliberately trips the striker purely to stop the goalscoring opportunity — a foul sometimes informally called a 'professional foul'. Why might commentators use this specific informal term?",
 "options": [
   "It refers to a foul committed deliberately and calculatedly, as a tactical decision to prevent a clear goal, accepting a card as the tradeoff, rather than being a genuine, spontaneous mistimed challenge for the ball itself",
   "It refers specifically to any foul committed exclusively by a player who happens to be employed on a full-time professional contract, as opposed to any foul committed by an amateur or semi-professional player in a lower-level match",
   "It refers to a type of foul that is claimed to actually be fully legal and permitted under the current laws of the game, with the informal term itself existing purely as unofficial media commentary slang with no actual real disciplinary implication",
   "It refers to a foul that can only occur during a professional, officially sanctioned competition, and is claimed to be structurally impossible to occur in any youth, school, or amateur match under any circumstances"
 ],
 "answer": 0,
 "explanation": "A 'professional foul' is informal terminology for a deliberate, calculated foul made specifically to stop a clear goalscoring opportunity, with the fouling player effectively accepting a card as an acceptable tradeoff — distinguishing it from a genuine, spontaneous mistimed challenge where the defender was actually attempting to win the ball fairly."
},
{
 "q": "A match referee, assessing a serious challenge, considers factors including the amount of force used, whether the opponent's safety was endangered, and whether the tackle was reckless or made with excessive force, before deciding between a yellow card, a red card, or no card at all. What does this process illustrate about how disciplinary decisions are actually made?",
 "options": [
   "Disciplinary decisions for challenges involve genuine judgement weighing multiple specific factors (force, intent, danger to the opponent), rather than being a simple, automatic, purely mechanical lookup based on one single isolated factor alone",
   "Disciplinary decisions for challenges of this kind are claimed to be made entirely at random by the referee, with genuinely no consistent underlying factors, criteria, or reasoning actually considered in any real decision of this kind",
   "Every single physical challenge between two opposing players, regardless of its specific individual nature, force, or context, automatically and always results in an identical yellow card being shown under current laws",
   "Only the very final resulting outcome of a specific challenge — meaning specifically whether or not the challenged player actually gets injured as a direct result — is ever considered relevant to any disciplinary decision made by a referee"
 ],
 "answer": 0,
 "explanation": "Real disciplinary decisions for challenges involve genuine judgement across multiple factors — force used, danger posed to the opponent, whether the challenge was reckless or simply mistimed — which is exactly why identical-looking physical contests can reasonably result in different outcomes (no card, yellow, or red) depending on the actual specific circumstances of each individual challenge."
},
{
 "q": "Which of the following are genuine, correct applications of the offside law as currently written? Select all that apply.",
 "options": [
   "A player exactly level with the second-last defender at the moment the ball is played is not offside",
   "A player cannot be penalised for offside directly from a throw-in",
   "Simply standing in an offside position is itself always an offence, regardless of whether the player becomes involved in play",
   "A deliberate play of the ball by a defender can reset the offside phase for a previously offside attacker"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Being exactly level (not offside), the throw-in exception, and a defender's deliberate play resetting the phase are all genuine, correct rules. The claim that merely standing in an offside position is itself always an offence is false — a player is only penalised for offside if they become actively involved in play from that position."
},
{
 "q": "Which of the following are recognised sending-off (red card) offences under the laws of the game? Select all that apply.",
 "options": [
   "Denying an obvious goalscoring opportunity through an offence, wherever on the pitch it occurs",
   "Serious foul play, such as using excessive force or endangering an opponent's safety in a challenge",
   "Receiving a second caution (yellow card) in the same match",
   "Simply being on the losing team at the final whistle, regardless of any specific individual conduct during the match"
 ],
 "answer": [0, 1, 2],
 "multi": True,
 "explanation": "Denying an obvious goalscoring opportunity, serious foul play, and a second caution in the same match are all genuine, recognised sending-off offences. Simply being on the losing team has no disciplinary relevance whatsoever — red cards are based on individual conduct during the match, not on the eventual final result."
},
{
 "q": "A cup competition's rules once meant that if the two-legged aggregate score was tied, the team who scored more goals away from home over the two legs would advance, without needing extra time or penalties. Many major competitions, including UEFA's, have since abolished this rule. What was it commonly called, and why might a governing body choose to remove it?",
 "options": [
   "The away goals rule — abolished by UEFA partly because it was felt to distort tactics (sometimes discouraging the home team in the second leg from attacking) rather than genuinely reflecting which team was actually better over two matches",
   "The golden goal rule — a completely different concept referring specifically to the first goal scored in extra time immediately ending a match, rather than to any rule about weighting goals scored away from home across two separate legs",
   "Away goals rules of this kind are claimed to have never actually existed in any real competition, making this entire scenario a purely hypothetical, invented example with no connection to any real historical football rule change",
   "The offside rule — a completely unrelated law about attacking players' positioning relative to defenders, which has no connection whatsoever to any rule about weighting goals scored away from home across a two-legged tie"
 ],
 "answer": 0,
 "explanation": "The away goals rule gave extra weight to goals scored away from home in a tied two-legged tie. UEFA abolished it from the 2021-22 season onward, partly over concern that it distorted tactics — sometimes discouraging a leading home team from attacking freely in the second leg — rather than reliably reflecting genuine overall quality across both matches."
},
{
 "q": "In an older version of the laws, the very first goal scored during extra time would immediately and automatically end the match, sometimes producing dramatic, sudden conclusions. This rule has since been removed from top-level competition. What was it called?",
 "options": [
   "The golden goal — an immediate-win rule for the first goal scored in extra time, since removed from top-level competition partly because it was felt to encourage overly cautious, defensive extra-time play rather than open, attacking football",
   "The away goals rule — a completely different rule about weighting goals scored away from home across a two-legged tie, unrelated to any rule about a single decisive goal immediately ending a match during extra time",
   "VAR (Video Assistant Referee) — a technology used to review and correct clear and obvious errors in refereeing decisions, an entirely different modern concept unrelated to any historical rule about extra time ending immediately",
   "The offside rule — a completely unrelated law about attacking players' positioning relative to defenders, with no connection whatsoever to any historical rule about a single decisive goal immediately ending a match"
 ],
 "answer": 0,
 "explanation": "The golden goal rule meant the first goal scored in extra time immediately and automatically won the match. It was removed from major competitions (including the World Cup and UEFA tournaments) partly because it was felt to actually encourage overly cautious, risk-averse extra-time play — teams fearing conceding the instant, match-ending goal — rather than the exciting, open football it was originally intended to produce."
},
{
 "q": "A penalty shootout is required to decide a knockout match after normal and extra time end level. Each team's first five kicks are taken alternately, and if still tied, the shootout proceeds to sudden death. What does 'sudden death' mean in this specific context?",
 "options": [
   "After the initial five kicks each, further rounds of one kick per team continue, with the shootout ending the moment one team has scored and the other has missed within the same single round, rather than requiring another full set of five",
   "The match itself must be immediately replayed in full from the very beginning on a different day, rather than continuing with any further individual penalty kicks taken beyond the original first five kicks per team",
   "Both teams are declared joint winners and the competition trophy is shared equally between them, rather than the shootout actually continuing with any further individual kicks taken by either team",
   "The two team captains settle the tie with a coin toss instead, rather than any further individual penalty kicks actually being taken by either team beyond the original first five kicks per team"
 ],
 "answer": 0,
 "explanation": "Sudden death in a penalty shootout means that after the initial five kicks each, further rounds proceed one kick per team, ending immediately once one team has scored and the other has missed within the exact same round — a shootout can therefore end after just one further kick each, rather than needing a complete additional set of five."
},
{
 "q": "A goalkeeper facing a penalty kick in a shootout stands still and doesn't move at all until the ball is actually struck, rather than guessing a direction early. What genuine strategic tradeoff does this specific approach involve?",
 "options": [
   "Waiting increases the chance of correctly reading where the actual kick is going once it's struck, but sacrifices the extra reaction time a keeper gains by committing early to a guessed direction, which is why some keepers instead choose to guess early based on a kicker's tendencies",
   "There is no genuine tradeoff involved in this specific approach at all, since a goalkeeper who waits until the ball is actually struck is claimed to always save the penalty with complete, guaranteed certainty regardless of where it's placed",
   "Goalkeepers are formally required under the laws of the game to always guess a direction and dive early before a penalty kick is actually struck, meaning waiting until contact is claimed to not actually be a legally permitted approach",
   "This approach guarantees the kick will always be missed by the penalty taker themselves, since a goalkeeper's own specific decision about when to move is claimed to have some kind of direct, guaranteed physical effect on the kicker's own accuracy"
 ],
 "answer": 0,
 "explanation": "This reflects a genuine, real strategic tradeoff goalkeepers actually weigh: reacting to the kick itself (waiting) gives more accurate information about where the ball is actually going, but sacrifices precious reaction time — which is exactly why some goalkeepers instead study a specific kicker's known tendencies and commit to a guessed direction early, accepting the risk of guessing wrong in exchange for more time to react if they guess right."
},
{
 "q": "A player is found to be wearing a metal necklace during a match, which match officials had not noticed during the pre-match equipment check. Once discovered, what is the standard handling of this kind of situation under player equipment regulations?",
 "options": [
   "The player is required to remove the dangerous item before being permitted to continue playing, since jewellery and other items capable of causing injury to the wearer or another player are restricted under player equipment regulations",
   "Nothing needs to happen at all in this situation, since jewellery of any kind is claimed to be fully and completely permitted without any restriction whatsoever under the current laws of the game and player equipment regulations",
   "The player is shown a straight red card and sent off immediately, since wearing any item of jewellery during a match is treated as serious foul play requiring an automatic dismissal under current equipment regulations",
   "The entire match must be immediately abandoned and restarted completely from the very beginning, since discovering a single piece of prohibited jewellery on any one player is treated as invalidating everything that occurred beforehand"
 ],
 "answer": 0,
 "explanation": "Player equipment regulations restrict jewellery and other items that could cause injury to the wearer or another player — a player discovered wearing something like a metal necklace during a match is generally required to remove it before continuing, a straightforward safety-driven equipment rule rather than a disciplinary or match-ending matter."
},
{
 "q": "The six-yard box (goal area) marked on a football pitch closest to each goal defines the area from which a goal kick must be taken. What is another key rule specifically associated with this particular marked area?",
 "options": [
   "It defines the zone within which an attacking player cannot legally be challenged for the ball once a goalkeeper has moved to collect it there under certain interpretations, and it marks where a goal kick is placed for the restart",
   "It marks the exact area of the pitch where the offside law is claimed to never apply at any point during a match, regardless of where the ball is actually played from during any given passage of open play",
   "It marks the specific area of the pitch reserved exclusively for any team's own designated captain to stand during a corner kick taken by the opposing team, unrelated to any goal kick or goalkeeper positioning rule",
   "It has no genuine rules-based significance of any kind whatsoever, and is claimed to exist purely as a cosmetic pitch marking with no actual bearing on how any restart or any goalkeeper interaction is legally conducted"
 ],
 "answer": 0,
 "explanation": "The six-yard box (goal area) is where a goal kick is placed for the restart, and it's also closely associated with goalkeeper protection — the area near where a keeper gathers the ball is where challenging them for possession they've already secured becomes an infringement, a related but separate rule from the box's role in defining the goal kick restart position."
},
{
 "q": "Two players from opposing teams run for a loose ball shoulder-to-shoulder, making fair, non-excessive physical contact within playing distance of the ball, and one player is knocked slightly off balance but neither commits any clearly reckless or dangerous action. What is the correct decision?",
 "options": [
   "No foul — a fair shoulder-to-shoulder challenge made within playing distance of the ball, without excessive force, is a legitimate part of the game and not an offence, even if one player ends up off balance as a result",
   "A direct free kick is awarded automatically to whichever specific player happened to actually end up off balance as a result of the challenge, regardless of whether the actual contact itself was genuinely fair or not",
   "Both players are shown yellow cards simultaneously, since any physical contact at all between two opposing players during a challenge for the ball is treated as a cautionable offence under the current laws of the game",
   "The referee is required to immediately abandon the match entirely, since physical contact of any kind occurring between two opposing players during any challenge is treated as serious enough to require ending the match"
 ],
 "answer": 0,
 "explanation": "A fair, shoulder-to-shoulder challenge made within playing distance of the ball, without excessive force, is a legitimate part of football and not a foul, even if it knocks an opponent slightly off balance — this genuine physical contest for the ball is a normal, accepted part of the game, distinct from a reckless or dangerous challenge."
},
{
 "q": "An attacking player, without the ball anywhere near them, deliberately stands in front of a defender to physically block their path and prevent them from reaching a teammate who's about to receive a pass, using their body but making no attempt to play the ball themselves. What is this generally judged as?",
 "options": [
   "Obstruction (impeding an opponent) — using the body to block an opponent's path without playing or attempting to play the ball is an offence, distinct from a fair shoulder-to-shoulder challenge made while actually contesting for the ball",
   "A completely fair and entirely legal tactic under all circumstances, since blocking an opponent's path with the body is claimed to always be fully permitted regardless of whether the blocking player ever makes any attempt to play the ball",
   "Serious foul play requiring an automatic straight red card, treating a simple, non-forceful obstruction of this kind identically to how a genuinely dangerous, forceful tackle endangering an opponent's safety would be treated",
   "A penalty kick offence, treating a fairly minor path-blocking obstruction occurring away from either penalty area identically to a genuine, serious foul actually committed inside a team's own penalty area"
 ],
 "answer": 0,
 "explanation": "Impeding an opponent (obstruction) — using the body to block a path without playing or attempting to play the ball — is an offence, genuinely distinct from a fair shoulder-to-shoulder challenge where a player is actually contesting for the ball itself rather than simply using their body purely to block another player's path."
},
{
 "q": "A player attempting an overhead kick raises their leg dangerously high with studs facing an onrushing opponent's head, even though no actual contact occurs because the opponent pulls back in time. How is this kind of near-miss dangerous action generally treated?",
 "options": [
   "It can still be penalised as dangerous play even without actual contact, since the offence is based on the genuine danger the action posed to an opponent's safety, not solely on whether contact actually happened to occur",
   "Nothing at all can be done in this situation, since an offence of any kind is claimed to only ever exist under the laws of the game if actual physical contact between the two players genuinely occurred at some point",
   "A goal is automatically awarded to the team of the player who attempted the dangerous overhead kick, regardless of the fact that the action itself was actually judged dangerous specifically toward an opponent's safety",
   "The entire match must be immediately abandoned in every single case where any player raises a foot dangerously high near any opponent at any point, regardless of whether any actual contact ever occurs between the two players"
 ],
 "answer": 0,
 "explanation": "Dangerous play can be penalised based on the genuine danger an action posed to an opponent's safety, even without actual contact — a high, studs-facing kick near an opponent's head is judged on the real risk it created, not solely on whether the opponent happened to avoid it in time, since waiting for actual contact would mean ignoring genuinely dangerous play that simply got lucky."
},
{
 "q": "A goalkeeper restarts play by throwing the ball out to a teammate rather than kicking it, and this is one of several legal methods of goalkeeper distribution recognised under the laws. Which of the following is also a legal way for a goalkeeper to release the ball back into open play after making a save?",
 "options": [
   "Kicking (a drop-kick or punt) — goalkeepers may legally distribute the ball with a throw, a kick, or by simply rolling it, giving them multiple legitimate options depending on the tactical situation",
   "Distribution methods are claimed to be entirely and completely restricted to exactly one single legally permitted method under the current laws of the game, with genuinely no other alternative distribution option available",
   "A goalkeeper is claimed to be legally required to always physically run the ball out to the edge of their own penalty area before releasing it in any way, rather than throwing, kicking, or rolling it directly from where they caught it",
   "A goalkeeper is claimed to be legally prohibited under current laws from ever using their foot to kick the ball as any part of a legal distribution method, being restricted exclusively to throwing or rolling it by hand instead"
 ],
 "answer": 0,
 "explanation": "Goalkeepers have multiple legal distribution options after gaining possession — throwing, kicking (a drop-kick or punt), or simply rolling the ball — giving them tactical flexibility to choose the method best suited to the specific situation, rather than being restricted to just one single method."
},
{
 "q": "A player is seriously injured during play and needs to be removed from the pitch on a stretcher for their own safety, requiring a significant stoppage in play. What is standard practice regarding how this stoppage is generally handled?",
 "options": [
   "Play is stopped for player safety, and the match resumes afterward with an appropriate restart (commonly a dropped ball, or the ball returned to the team in possession, depending on the specific competition's own practice), while the affected time is typically accounted for in stoppage time",
   "The match is always immediately and permanently abandoned the moment any player requires stretcher removal for any injury of any kind, regardless of the actual severity of that specific injury or how the rest of the match might otherwise have continued",
   "Play never actually stops for this kind of situation at all, since a serious injury requiring stretcher removal is claimed to never actually be considered sufficient grounds for the referee to stop play under the current laws of the game",
   "The injured player's entire team is immediately and automatically disqualified from the rest of the match purely as a result of that one player's own injury, regardless of how the injury itself actually occurred during play"
 ],
 "answer": 0,
 "explanation": "A serious injury requiring stretcher removal is genuine grounds to stop play for player safety — the match then resumes with an appropriate restart once the player has been safely removed, and the time lost to the stoppage is typically factored into the stoppage time added at the end of that half, rather than the match being abandoned outright for what remains a routine (if serious) in-game stoppage."
},
{
 "q": "A campaign in grassroots and youth football encourages only the team captain to speak to the referee about a decision, aiming to reduce abusive dissent from multiple players surrounding an official at once. What does this kind of initiative reflect about football's broader relationship with its referees?",
 "options": [
   "There's ongoing, active effort within football's culture and governance to protect match officials from abuse and improve the overall standard of conduct toward them, alongside (not replacing) the formal disciplinary rules already covering dissent",
   "This kind of initiative has no real, genuine connection whatsoever to the actual formal laws of the game, since anything related to respecting match officials is claimed to be considered a purely symbolic gesture with no practical effect on conduct",
   "It proves that referees in football have historically never actually faced any real form of abuse or disrespect from players at any level of the game, making the entire premise of any such initiative fundamentally unnecessary",
   "It means only team captains are now formally permitted to speak to a referee under any circumstances whatsoever, with every other single player on the pitch being completely and permanently barred from ever addressing any match official"
 ],
 "answer": 0,
 "explanation": "'Respect' style campaigns (widely run at various levels of football, especially grassroots and youth) reflect a genuine, ongoing effort within football's broader culture to reduce abuse toward officials and improve conduct — a cultural and educational initiative that works alongside, not instead of, the formal disciplinary rules that already exist specifically to sanction dissent."
},
{
 "q": "A referee awards a free kick to the attacking team for a foul, and while the ball is being placed, an opposing player deliberately kicks it away to delay the restart. What offence has been committed, and what is the typical sanction?",
 "options": [
   "Delaying the restart of play (or failing to respect the required distance) — a cautionable offence, typically resulting in a yellow card for the player who deliberately kicked the ball away to waste time",
   "No offence has actually been committed at all in this situation, since deliberately kicking the ball away after a free kick has been awarded is claimed to be considered a fully normal, unremarkable part of the game with no disciplinary consequence",
   "The offending player is shown a straight red card and sent off immediately, since deliberately kicking a ball away after a free kick has been awarded is treated as serious foul play under current laws of the game",
   "The free kick is automatically cancelled and downgraded to a much less advantageous throw-in instead, purely because the opposing player deliberately kicked the ball away to delay the restart of play in this specific instance"
 ],
 "answer": 0,
 "explanation": "Deliberately kicking the ball away after a free kick has been awarded is a recognised cautionable offence — a yellow card is the standard, proportionate sanction for this kind of deliberate delay, giving the referee a clear tool to discourage this specific and fairly common time-wasting tactic."
},
{
 "q": "A goalkeeper deliberately handles a ball played back to them not directly by a teammate's foot, but from a throw-in taken by that same teammate. What is the correct decision?",
 "options": [
   "No offence — the back-pass restriction on goalkeepers handling the ball specifically applies to the ball being deliberately kicked by a teammate's foot, and does not apply to the ball being received directly from a teammate's throw-in",
   "An indirect free kick is awarded to the opposing team, since the back-pass restriction is claimed to apply identically and equally to absolutely any deliberate delivery from a teammate, including a throw-in, with no distinction made based on delivery method",
   "A penalty kick is awarded automatically to the opposing team, treating a goalkeeper handling the ball from a teammate's throw-in identically to a genuine deliberate-kick back-pass violation occurring inside the penalty area",
   "The goalkeeper is shown a straight red card and sent off immediately, since handling a ball received from a teammate's throw-in is treated as serious foul play requiring an automatic dismissal under current laws of the game"
 ],
 "answer": 0,
 "explanation": "This is a specific, deliberately carved-out exception within the back-pass law: the restriction on a goalkeeper using their hands applies specifically to the ball being kicked to them by a teammate's foot — a ball received directly from a teammate's throw-in is explicitly exempted, meaning the goalkeeper may legally handle it."
},
{
 "q": "A referee's assistant (linesman) is responsible for signalling offside, throw-ins, and other decisions along their designated half of the touchline, working in coordination with the main referee rather than making decisions entirely independently. What does this division of responsibility illustrate about how top-level matches are actually officiated?",
 "options": [
   "Match officiating is a coordinated team effort, with different officials assigned specific zones and responsibilities that combine to cover the full pitch, rather than being the sole individual responsibility of one single referee acting entirely alone",
   "The assistant referee's decisions are claimed to always be treated as final, absolute, and binding regardless of the main referee's own contrary judgement, meaning the main referee effectively has no independent authority once an assistant has signalled a decision",
   "Assistant referees are claimed to have no genuine formal role or responsibility whatsoever in officiating a match, existing purely as a ceremonial, non-functional position with no actual bearing on any real decision made during play",
   "A single assistant referee is claimed to be solely and completely responsible for covering the entire pitch on their own, with the main referee restricted exclusively to a single small area near the very centre of the pitch"
 ],
 "answer": 0,
 "explanation": "Officiating a match is a coordinated team effort — assistant referees cover specific zones and specific responsibilities (like offside along their half of the touchline), feeding information to the main referee, who retains overall decision-making authority — rather than either one official trying to single-handedly cover an entire pitch alone or an assistant's signal being treated as automatically final regardless of the referee's own judgement."
},
{
 "q": "A team is awarded an indirect free kick just a few yards outside the opposing goalkeeper's six-yard box, in a very promising position. Why might this specific type of free kick be considered tactically trickier to convert into a goal than an equally well-positioned direct free kick?",
 "options": [
   "Because an indirect free kick cannot result in a goal from the kick itself — the ball must touch a second player first — requiring the attacking team to work a genuine passing combination rather than simply shooting straight at goal",
   "Because indirect free kicks are claimed to always be taken from a position significantly further away from the goal than any direct free kick, regardless of the actual specific location where the underlying foul originally occurred",
   "Because the goalkeeper is claimed to be legally permitted to physically stand directly in front of the ball itself specifically during an indirect free kick, unlike during any direct free kick, which has no such allowance",
   "Because indirect free kicks are claimed to always require at least five different separate attacking players to each individually touch the ball in sequence before any shot at goal is legally permitted to be attempted"
 ],
 "answer": 0,
 "explanation": "An indirect free kick specifically cannot result in a goal directly from the kick itself — the ball must touch a second player (from either team) before a goal counts — which means the attacking team has to work a genuine passing combination or set-piece routine, giving the defending team a clearer, more predictable structure to organise against compared to defending a direct shot on goal."
},
{
 "q": "A defender, defending a corner kick, deliberately and forcefully pulls back on an attacking opponent's shirt to prevent them from jumping freely to meet the ball, and the referee spots the infringement clearly. What is the correct decision?",
 "options": [
   "A direct free kick (or penalty, since this occurred inside the penalty area from a corner) is awarded to the attacking team, since holding or pulling an opponent is a direct free kick offence, and inside the box that means a penalty kick",
   "No offence at all is called in this situation, since physical contact of any kind between two opposing players contesting for a corner kick delivery is claimed to always be considered a fully normal, unremarkable part of the game",
   "An indirect free kick only is awarded, treating a deliberate, forceful shirt-pull identically to a minor, incidental positioning infringement rather than to the direct free kick (and inside the box, penalty) offence that holding actually is",
   "The corner kick must simply be retaken from the exact same corner, with no further disciplinary or restart consequence at all applied to the defender who was actually responsible for the deliberate shirt-pulling infringement"
 ],
 "answer": 0,
 "explanation": "Holding or pulling an opponent (including a shirt-pull to prevent a free jump) is a direct free kick offence — when it happens inside the penalty area, as is common at a defended corner, that means a penalty kick for the attacking team, not merely an indirect free kick or a simple retake with no consequence."
},
{
 "q": "A referee, having already shown several cards during a physical match, notices the overall tone becoming increasingly ill-tempered and calls both team captains together for a brief, calm word about managing their players' conduct, rather than immediately reaching for more cards. What does this illustrate about effective refereeing beyond simply enforcing the written laws?",
 "options": [
   "Effective refereeing often includes genuine game management — communication and de-escalation — alongside strict law enforcement, since consistently reaching for cards alone doesn't always address the underlying tension driving a match's deteriorating tone",
   "This kind of communication with team captains is claimed to be entirely and formally prohibited under the laws of the game, meaning any referee doing this would actually be acting improperly and outside their own legitimate authority",
   "It proves that the referee in this specific scenario is failing at their job, since the sole and only legitimate tool available to any referee for managing a match's conduct is claimed to be showing cards, with no other approach considered valid",
   "It has no real practical value or effect whatsoever on how a match's overall conduct or tone might actually develop for the remainder of play, regardless of what the referee actually chooses to say to either team's captain"
 ],
 "answer": 0,
 "explanation": "Skilled referees genuinely use game management — clear communication, timely words with captains, proactive de-escalation — as a real complement to strict law enforcement, since consistently reaching only for cards doesn't always address the underlying tension driving a match's deteriorating tone, while a well-timed conversation sometimes can."
},
{
 "q": "A team's designated penalty taker steps up to take a penalty kick during regular play (not a shootout), strikes the ball, and it rebounds back into play off the goalkeeper's save. What is the correct rule regarding who may then play the rebounding ball?",
 "options": [
   "Any player, including the original kicker, may play the rebound once it's back in open play during a regular in-game penalty, unlike in a shootout, where the kicker generally cannot play a second touch on a rebound",
   "The original penalty taker is claimed to be strictly and permanently forbidden from ever touching the ball again for the remainder of the entire match once they have taken a penalty kick during regular play, regardless of any rebound",
   "The rebound is claimed to always automatically result in a goal kick for the defending team regardless of what actually happens to the ball after the goalkeeper's save, with no further open play ever permitted to continue",
   "The rebound is claimed to always automatically result in a corner kick for the attacking team regardless of what actually happens to the ball after the goalkeeper's save, with no further open play ever permitted to continue"
 ],
 "answer": 0,
 "explanation": "During regular open play, a penalty kick that rebounds off the goalkeeper (or the goal frame) remains live, and any player — including the original penalty taker — may play the rebound, since it's simply continuing open play. This differs from a penalty shootout, where the kicker is generally not permitted to play a second touch on their own rebound."
},
{
 "q": "A defender attempts to play the ball but instead makes contact with an opponent's leg first, in what the referee judges to be a careless (rather than reckless or excessive-force) challenge — a genuine mistimed attempt to win the ball, not an unfair or dangerous one. What is the most likely correct outcome?",
 "options": [
   "A direct free kick (or penalty if inside the area) without any card, since a careless but genuine attempt to play the ball is a foul but doesn't automatically rise to the level of a cautionable or sendable offence unless it's also reckless or uses excessive force",
   "A straight red card and immediate sending-off, treating a careless, genuinely mistimed challenge identically to how a reckless or excessive-force challenge that endangers an opponent's safety would actually be treated",
   "No foul is called at all in this situation, since a challenge specifically judged by the referee to be merely careless, rather than reckless or dangerous, is claimed to never actually be considered any kind of offence whatsoever",
   "The match must be immediately abandoned entirely, since any physical contact at all between two opposing players attempting to challenge for the ball is treated as serious enough on its own to require ending the match"
 ],
 "answer": 0,
 "explanation": "The laws distinguish between careless (a genuine, mistimed attempt still resulting in a foul but no card), reckless (warranting a caution), and excessive force endangering safety (warranting a red card) — a careless challenge is still a foul, giving away the free kick or penalty, but doesn't automatically escalate to a card unless the referee judges it crosses into recklessness or danger."
},
{
 "q": "Which of the following are genuine, correct facts about penalty kicks, whether taken during regular play or in a shootout? Select all that apply.",
 "options": [
   "The goalkeeper must have at least part of one foot on or in line with the goal line at the moment the kick is taken",
   "Any eligible player from the attacking team, not necessarily the player who was fouled, may take a regular in-game penalty kick",
   "A penalty kick is always guaranteed to result in a goal, since the laws of the game formally prohibit the goalkeeper from making any save",
   "In a shootout specifically, the original kicker generally cannot play a rebound off their own attempted kick"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "The goalkeeper's foot-position requirement, the freedom to choose any eligible kicker for a regular in-game penalty, and the shootout-specific rebound restriction are all genuine, correct rules. The claim that a penalty is guaranteed to result in a goal is obviously false — goalkeepers are permitted, and frequently do, save penalty kicks."
},
{
 "q": "Which of the following restarts require the ball to be put back into play in a way that could result in a goal being scored directly, without needing to touch another player first? Select all that apply.",
 "options": [
   "A direct free kick",
   "A penalty kick",
   "A corner kick",
   "An indirect free kick"
 ],
 "answer": [0, 1, 2],
 "multi": True,
 "explanation": "Direct free kicks, penalty kicks, and corner kicks can all result in a goal scored straight from the restart, with no need for another player to touch the ball first. An indirect free kick is the specific exception — it requires the ball to touch a second player, from either team, before a goal can be legally awarded."
},
{
 "q": "A player celebrating a goal removes their shirt and waves it toward the crowd, and the referee shows them a yellow card immediately afterward, despite the goal itself standing. What does this specific combination of outcomes illustrate?",
 "options": [
   "A goal and a disciplinary caution for something that happened afterward are two separate, independent matters — the goal stands because it was legally scored, while the shirt removal is separately cautioned as excessive celebration under current laws",
   "The goal must actually be disallowed retroactively because of the player's own subsequent celebration, since the laws of the game are claimed to treat the goal and the celebration afterward as one single, combined, inseparable event",
   "The yellow card shown is claimed to actually be a refereeing mistake in every single case of this kind, since celebrating a goal by removing a shirt is claimed to never actually be considered any kind of cautionable offence under current laws",
   "The match must be immediately abandoned entirely, since a player removing their shirt to celebrate a goal is treated as serious enough on its own to require the referee to end the match altogether"
 ],
 "answer": 0,
 "explanation": "The goal and the celebration are treated as two separate matters: the goal stands because it was legally scored, while shirt removal is specifically listed as a cautionable offence under excessive celebration — a detail that surprises fans unfamiliar with it, since a genuinely legal goal can still be followed by a yellow card for what the scorer does immediately afterward."
},
{
 "q": "A defending team's goalkeeper takes a goal kick, and the ball travels the required distance out of the penalty area before a strong gust of wind blows it back inside the box, where a defender then plays it. Is this a violation of the requirement that the ball must leave the penalty area before being touched again?",
 "options": [
   "No violation — the ball did leave the penalty area as required before being played again by another player; wind pushing it back afterward doesn't retroactively undo the fact that the restart requirement was already satisfied at that point",
   "Yes, this is always considered a clear violation requiring the goal kick to be retaken, since the ball's final resting position at the exact moment it is actually touched is claimed to be the only factor that matters under current laws",
   "The referee is required to immediately abandon the match entirely in this specific situation, since a genuinely unusual weather-related event of this kind is treated as serious enough on its own to require ending the entire match",
   "A penalty kick must be awarded automatically to the attacking team in this specific situation, treating a defender touching a wind-blown ball back inside their own box identically to a genuine penalty-area foul"
 ],
 "answer": 0,
 "explanation": "The requirement is that the ball leaves the penalty area before being touched by another player — once that condition has genuinely been met, a gust of wind blowing it back in afterward doesn't retroactively undo the fact that the restart was already properly and legally completed at that point."
},
{
 "q": "A club's youth academy match trials a 'sin bin' system, where a player shown a yellow card must leave the pitch for a temporary period (commonly around 10 minutes) rather than simply continuing to play with a caution recorded. What is the main reasoning behind experimenting with this kind of temporary dismissal at grassroots and youth level?",
 "options": [
   "It gives referees an intermediate sanction between a yellow card (which has no immediate on-field consequence beyond the caution itself) and a full sending-off, aiming to more effectively deter dissent and reckless play, particularly in the developmental grassroots and youth game",
   "It is claimed to have no genuine underlying reasoning whatsoever behind it, and is claimed to exist purely as an arbitrary experimental gimmick with no actual real, practical, or disciplinary purpose behind its introduction at any level of football",
   "It is claimed to be a full and complete permanent replacement for the yellow card system at every single level of football worldwide, including at the very top level of the professional game, rather than a trial specifically limited to grassroots and youth football",
   "It is claimed to exist purely to intentionally shorten the overall total duration of any match in which it is used, with genuinely no connection whatsoever to disciplinary deterrence or to any specific player's own individual conduct on the pitch"
 ],
 "answer": 0,
 "explanation": "Sin bin trials (used at various grassroots and youth levels, distinct from the professional top flight where they remain far less common) aim to give referees a meaningful intermediate sanction — since a standard yellow card currently has no immediate on-field consequence beyond the caution itself, a temporary dismissal is intended to more effectively deter dissent and reckless play, particularly in the developmental game."
},
]
