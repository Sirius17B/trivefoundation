# Robotics — 30 questions, applied-reasoning style. Options are written at
# comparable length/detail so the correct answer can't be spotted by being
# the longest; distractors are plausible misconceptions, not throwaways.
QUESTIONS = [
{
 "q": "A chess-playing AI can beat a grandmaster, but a robot still struggles to reliably pick up an unfamiliar mug from a cluttered table — a task any toddler manages easily. What does this contrast best illustrate?",
 "options": [
   "Moravec's paradox — tasks that feel effortless to humans (like grasping) rely on enormous implicit sensorimotor knowledge built over evolution, making them far harder for machines than clearly bounded, rule-based tasks like chess",
   "Chess-playing AIs are fundamentally more advanced pieces of technology than any robot ever built, which is why comparing the two tasks is not actually meaningful in any way",
   "Robots are physically incapable of ever manipulating objects that were not specifically manufactured and designed for robots to handle in the first place",
   "The mug-grasping task must be a poorly designed test, since any task a toddler can do should logically also be simple for a sufficiently capable robot to do"
 ],
 "answer": 0,
 "explanation": "Hans Moravec's observation (1988) is that sensorimotor skills humans perform unconsciously — grasping unfamiliar objects, balancing while walking — draw on millions of years of evolved implicit knowledge, making them surprisingly hard to replicate computationally, while abstract tasks like chess are comparatively bounded and algorithm-friendly."
},
{
 "q": "A cleaning robot placed in a brand-new house has no map and no GPS signal indoors, yet within a few minutes builds a usable map of the rooms while also tracking its own position on that map. What is this core capability called?",
 "options": [
   "SLAM (Simultaneous Localisation and Mapping) — solving the 'where am I' and 'what does this space look like' problems together using onboard sensor data",
   "Inverse kinematics — computing which joint angles are needed to place a robot's end effector at a specific target location within the room",
   "Teleoperation — a human operator remotely guiding the robot's movement in real time from outside the house using a live camera feed",
   "Swarm robotics — many simple robots coordinating their movements together to collectively map a shared space faster than any one robot could alone"
 ],
 "answer": 0,
 "explanation": "SLAM lets a robot build a map of an unknown environment while simultaneously tracking its own position within that map — a genuine chicken-and-egg problem solved with probabilistic algorithms, and the foundation of how a single robot vacuum navigates an unfamiliar home without any pre-existing floorplan."
},
{
 "q": "A factory replaces a traditional robotic arm — which operates inside a locked safety cage because it moves fast and can't sense nearby humans — with a newer arm that senses contact and stops instantly, letting it work directly alongside people. What is this newer category of robot called?",
 "options": [
   "A collaborative robot (cobot) — designed with force/torque sensing to work safely in shared space with humans, unlike traditional industrial robots that must be physically separated",
   "An autonomous mobile robot (AMR) — designed to navigate freely around a warehouse floor using its own onboard sensors rather than following any fixed physical track",
   "A soft robot — built from flexible, compliant materials specifically so that any accidental contact with a human causes no injury regardless of the robot's speed",
   "A digital twin — a virtual simulation of the original caged robotic arm used to test new configurations safely before deploying them physically on the factory floor"
 ],
 "answer": 0,
 "explanation": "Cobots use force and torque sensing to detect unexpected contact and stop immediately, which is specifically what allows them to work directly alongside people without the safety cage traditional high-speed industrial robots require."
},
{
 "q": "An engineering team trains a robot to walk using a physics simulator for months, achieving a perfect, stable gait — but the very same robot falls over almost immediately when it first tries to walk on a real floor. What most directly explains this gap?",
 "options": [
   "The sim-to-real gap — simulations can't perfectly model real-world friction, sensor noise, and material properties, so skills learned purely in simulation don't always transfer cleanly to physical hardware",
   "The robot's physical motors must be defective, since a robot that walks perfectly in any simulation is guaranteed by definition to also walk perfectly in the real world without any further adjustment",
   "Simulated training is fundamentally useless for any real robotics application, meaning the engineering team wasted their time and should have trained entirely on the real robot from the very first day",
   "The robot's onboard software was never actually connected to its physical motors during the simulation phase, which is why the simulated walking behaviour never had any chance of transferring"
 ],
 "answer": 0,
 "explanation": "Physics simulations are cheap and safe for training but can never perfectly capture every real-world detail — friction coefficients, sensor noise, material flex — so a policy that looks flawless in simulation can fail on first contact with reality, which is exactly why techniques like domain randomisation exist to help close this gap."
},
{
 "q": "An aircraft manufacturer maintains a continuously updated virtual model of a specific physical jet engine, fed live data from sensors on the real engine, allowing them to predict maintenance needs before a failure happens. What is this virtual model called?",
 "options": [
   "A digital twin — a virtual replica of a physical system, kept synchronised with real sensor data, used for monitoring, testing, and prediction without risking the physical system itself",
   "A foundation model — a broadly trained AI system adapted afterward for many different specific downstream applications across different industries and use cases",
   "An end effector — the specific tool or component attached to the end of a robotic arm that physically interacts with objects in the arm's environment",
   "A cobot — a robot specifically designed to operate safely in a shared physical workspace directly alongside human engineers and maintenance technicians"
 ],
 "answer": 0,
 "explanation": "A digital twin mirrors a specific physical system in software, continuously updated with real sensor data, allowing engineers to monitor, test scenarios, and predict issues (like an engine fault) without touching or risking the actual physical hardware."
},
{
 "q": "Amazon's warehouse picking robots handle standard boxed items well but still struggle to reliably pick irregularly shaped, unfamiliar items like a loose bag of produce. What core robotics challenge does this expose?",
 "options": [
   "Robot grasping of novel objects — determining a stable, appropriate grip requires simultaneously reasoning about an unfamiliar object's geometry, material, weight, and fragility, something humans do unconsciously but remains genuinely hard for robots",
   "Path planning — the challenge of computing a collision-free route for the robotic arm to travel from its starting position to the location of the item on the warehouse shelf",
   "Teleoperation — the difficulty of having a remote human operator control the robotic arm precisely enough in real time to successfully grasp any irregularly shaped item",
   "The uncanny valley — the discomfort human warehouse workers feel when watching a robot attempt to handle food items that closely resemble something a person would normally handle"
 ],
 "answer": 0,
 "explanation": "Grasping unfamiliar, irregularly shaped objects requires reasoning jointly about geometry, material properties, and stability in real time — something humans do intuitively without conscious calculation, but which remains a genuinely unsolved research problem for robots handling truly novel items."
},
{
 "q": "A team deploys 50 small, simple robots into a collapsed building, each following basic local rules like 'avoid obstacles' and 'report open spaces', and together they map the disaster site far faster than any single larger robot could alone. What is this coordination approach called?",
 "options": [
   "Swarm robotics — many simple robots following local rules producing complex, useful collective behaviour without any single central controller directing them",
   "Sim-to-real transfer — training each of the fifty robots individually in a simulated collapsed-building environment before deploying them into the real disaster site",
   "Inverse kinematics — computing the specific joint angles each of the fifty robots would need to reach every point of interest within the collapsed structure",
   "A digital twin — maintaining one single, continuously updated virtual replica of the collapsed building that each of the fifty physical robots refers back to"
 ],
 "answer": 0,
 "explanation": "Swarm robotics, inspired by ant colonies and bird flocking, relies on simple local rules producing useful emergent global behaviour with no central controller — well suited to search-and-rescue, where many cheap, expendable robots exploring in parallel beats one expensive robot exploring alone."
},
{
 "q": "A hyper-realistic humanoid robot with lifelike skin and facial movements makes people feel more unsettled than either a clearly mechanical robot or a cartoonish robot like Pepper. What is this discomfort effect called, and why do many social robots deliberately avoid photorealism?",
 "options": [
   "The uncanny valley — as robots become more human-like, comfort rises then drops sharply once they're close-but-not-quite human, which is exactly why many designers keep social robots deliberately cartoonish",
   "Sim-to-real transfer — the discomfort stems from the robot behaving differently in the real world than it did during its original training and testing simulations before deployment",
   "Model collapse — repeated design refinements of a humanoid robot's face over successive prototype generations gradually degrade how natural and appealing the design ultimately looks",
   "Moravec's paradox — the observation that tasks like producing convincingly humanlike facial expressions are surprisingly difficult for robots despite seeming simple to design"
 ],
 "answer": 0,
 "explanation": "Masahiro Mori's uncanny valley (1970) describes how human comfort with robots rises with human-likeness, then drops sharply just before the resemblance becomes near-perfect — which is why deliberately non-photorealistic, cartoonish designs like Pepper often feel more comfortable than a robot that almost, but not quite, looks fully human."
},
{
 "q": "A worker with a spinal cord injury regains the ability to stand and walk short distances using a wearable robotic device strapped to their legs that assists their movement. What category of robotic technology is this?",
 "options": [
   "An exoskeleton — a wearable robotic structure that augments or restores human movement, used both medically for rehabilitation and industrially to reduce worker fatigue and injury risk",
   "A cobot — a robotic arm specifically designed to work directly alongside a human in a shared industrial or warehouse workspace rather than being worn on the human's own body",
   "An autonomous mobile robot (AMR) — a wheeled or legged robot that independently navigates a space using its own onboard sensors without requiring a human to wear or direct it",
   "A digital twin — a virtual, software-based replica of the worker's own body used to simulate and test possible rehabilitation and mobility-assistance strategies before physical use"
 ],
 "answer": 0,
 "explanation": "Exoskeletons are wearable robotic structures that augment or restore human movement — medical versions (like Ekso, ReWalk) help people with spinal injuries stand and walk, while industrial versions reduce fatigue and injury risk for workers doing repetitive heavy lifting."
},
{
 "q": "A robot assembling small electronic components can 'feel' when a connector clicks properly into place, and adjusts its grip pressure so it doesn't crush a delicate part. Which technology gives it this kind of tactile awareness?",
 "options": [
   "Force-torque sensing — sensors at the wrist or gripper that measure applied forces and torques, giving the robot a functional sense of touch for tasks requiring delicate handling or detecting unexpected contact",
   "SLAM — simultaneous localisation and mapping, which lets the robot build a map of the assembly area while tracking its own position relative to the components on the table",
   "Swarm robotics — coordination between multiple simple robots each handling a small part of the overall assembly task using local rules rather than any centralised sensing system",
   "The uncanny valley — a design consideration about how human-like a robot's appearance should be, which becomes relevant whenever a robot works closely alongside human assembly workers"
 ],
 "answer": 0,
 "explanation": "Force-torque sensing gives robots a functional sense of touch, letting them detect subtle cues like a connector clicking into place or excessive pressure before it damages a delicate component — critical for assembly tasks that require 'feel', not just precise positioning."
},
{
 "q": "Rather than writing detailed code specifying every joint angle for a welding path, a technician physically guides a robotic arm through the desired motion once, and the robot replays that exact path afterward. What is this teaching method called, and why does it matter?",
 "options": [
   "Programming by demonstration — teaching a robot a task by physically guiding it through the motion rather than writing explicit code, making robot deployment accessible to people who aren't specialist programmers",
   "Reinforcement learning — training the robot through repeated trial and error, rewarding successful welds and penalising failed ones until it gradually discovers the desired path on its own",
   "Federated learning — combining welding-path data gathered from many separate robotic arms at different factories into one shared, centrally trained model without moving any raw data",
   "Sim-to-real transfer — first training the exact welding motion inside a physics simulator, then deploying the resulting learned policy onto the real physical welding robot"
 ],
 "answer": 0,
 "explanation": "Programming by Demonstration lets a robot learn a task from a physically guided example rather than hand-written code specifying every joint angle, which meaningfully lowers the barrier to deploying robots for tasks like welding beyond teams with specialist robotics programmers."
},
{
 "q": "To pick up an object at a specific point in space with a specific gripper orientation, a robotic arm's controller must calculate exactly what angle each of its joints needs to be set to. What is this calculation called?",
 "options": [
   "Inverse kinematics — computing the joint angles required to place the end effector at a desired position and orientation, which is computationally challenging because multiple valid solutions can exist",
   "Forward kinematics — computing where the robotic arm's end effector ends up in space, given a specific, already-known set of joint angles as the starting input to the calculation",
   "SLAM — simultaneously building a map of the surrounding environment while tracking the robotic arm's own position and joint configuration relative to that constructed map",
   "Teleoperation — a human operator remotely specifying, in real time, each individual joint angle needed for the robotic arm to reach the desired target position and orientation"
 ],
 "answer": 0,
 "explanation": "Inverse kinematics is the reverse of forward kinematics: instead of computing where the end effector ends up given known joint angles, it computes what joint angles are needed to reach a desired position and orientation — a genuinely hard computational problem since multiple valid joint configurations, or none at all, can exist for a given target."
},
{
 "q": "A hospital delivery robot navigates hallways by building its own map and planning routes in real time, easily adapting when a cart is left blocking its usual path — unlike an older factory robot that follows a fixed magnetic strip on the floor and simply stops if anything blocks that exact strip. What distinguishes the hospital robot?",
 "options": [
   "It's an autonomous mobile robot (AMR), which creates its own maps and plans real-time routes, unlike an Automated Guided Vehicle (AGV) that follows a predefined physical track and can't adapt to unexpected obstacles",
   "It's a cobot, specifically engineered to work directly alongside human medical staff in close physical proximity, which is the specific feature that allows it to avoid the blocked cart",
   "It's using swarm robotics, coordinating with a large number of other simple robots throughout the hospital to collectively determine the best alternative route around the blocked cart",
   "It's using a digital twin of the hospital building, which allows it to plan alternate routes only because the building's floorplan was pre-loaded rather than being learned by the robot itself"
 ],
 "answer": 0,
 "explanation": "AGVs (Automated Guided Vehicles) follow fixed physical tracks or magnetic tape, reliable in controlled settings but brittle to unexpected obstacles. AMRs build their own maps and plan routes in real time, letting them flexibly navigate dynamic, changing environments like a busy hospital corridor — which is exactly the described difference."
},
{
 "q": "A robot gripper made from flexible silicone can gently pick up a ripe tomato without bruising it, and can squeeze through a gap too narrow for a rigid metal claw. What robotics approach does this illustrate?",
 "options": [
   "Soft robotics — using compliant, flexible materials rather than rigid metal components, inspired by biological organisms, enabling safe handling of delicate objects and movement through tight or irregular spaces",
   "Teleoperation — a human operator remotely and manually adjusting the gripper's exact pressure in real time for each individual tomato being picked, rather than the gripper acting autonomously",
   "SLAM — the gripper simultaneously builds a map of each tomato's exact surface shape while tracking its own position relative to that specific tomato during the picking process",
   "Inverse kinematics — calculating the precise joint angles of a rigid robotic arm needed to approach and grip the tomato from the single most structurally optimal angle available"
 ],
 "answer": 0,
 "explanation": "Soft robotics uses compliant materials that deform safely on contact, which is exactly what enables gentle handling of delicate produce and passage through gaps or irregular spaces that a rigid gripper or frame simply cannot manage — an approach directly inspired by how biological organisms interact with the world."
},
{
 "q": "During a nuclear cleanup operation too dangerous for a human to enter directly, an operator sits in a control room and manually drives a robotic arm's every movement in real time via a video feed and joystick controls. What is this mode of operation called?",
 "options": [
   "Teleoperation — a human directly and remotely controls a robot's actions in real time, used for tasks too dangerous, delicate, or distant for full human presence or full robot autonomy",
   "SLAM — the robotic arm simultaneously builds its own map of the nuclear site while independently tracking its own position within it, entirely without any real-time human input",
   "Swarm robotics — the task is being split across many simple robotic arms operating together using local coordination rules rather than being handled by one arm directed by one operator",
   "Programming by demonstration — the operator physically guided the robotic arm through this exact cleanup motion once beforehand, and it is now simply replaying that exact recorded path"
 ],
 "answer": 0,
 "explanation": "Teleoperation keeps a human directly in the control loop for tasks too dangerous, delicate, or remote for full autonomy — nuclear cleanup and deep-sea work are classic examples, alongside surgical robots like the da Vinci system, where the human's real-time judgement remains essential."
},
{
 "q": "A robotics team is choosing an end effector for a new pick-and-place robot that needs to handle both rigid boxed products and loose, irregularly shaped fruit on the same line. What does this decision most directly affect?",
 "options": [
   "What the robot can actually physically do — the end effector (gripper, suction cup, or other tool) attached to the arm's tip is what interacts with the environment, so choosing or changing it directly changes the robot's task capability",
   "How the robot calculates its own position within the warehouse, since end effector choice is the single technical factor that determines whether SLAM can function correctly for that robot",
   "Whether the robot is legally classified as a cobot or a traditional industrial robot, since end effector type is the specific regulatory criterion used to distinguish between those two categories",
   "How quickly the robot's onboard software can build a digital twin of the product line, since end effector hardware directly determines the software's digital-twin modelling speed"
 ],
 "answer": 0,
 "explanation": "The end effector is the robot's functional 'hand' — welding torches, grippers, suction cups, or surgical tools each enable entirely different tasks, so choosing the right end effector (or being able to swap it) directly determines what a given robot arm can physically accomplish, independent of its control software."
},
{
 "q": "A drone delivering blood supplies to a rural clinic must compute a route that avoids trees, power lines, and no-fly zones while reaching its destination efficiently, recalculating instantly if a new obstacle like a moving vehicle appears. What is this ongoing computation called?",
 "options": [
   "Path planning — the computational process of determining how a robot should move from a start point to a goal while avoiding obstacles, accounting for physical constraints and efficiency",
   "Programming by demonstration — a human operator physically flying the drone once along the exact intended delivery route in advance, which the drone then simply replays on every future flight",
   "Force-torque sensing — measuring the physical forces and torques acting on the drone's frame in flight in order to determine the safest possible route to the rural clinic",
   "The uncanny valley — evaluating how comfortable people in the rural community feel about the appearance and flight behaviour of the delivery drone as it approaches the clinic"
 ],
 "answer": 0,
 "explanation": "Path planning algorithms (like A*, RRT, or D*) compute collision-free routes through an environment, accounting for both static known obstacles and dynamic ones detected in real time — exactly the kind of calculation a delivery drone needs to run continuously, not just once before takeoff."
},
{
 "q": "Which of the following are genuine, well-documented reasons robot grasping of novel, everyday objects remains a harder unsolved problem than many people assume? Select all that apply.",
 "options": [
   "The robot must estimate an unfamiliar object's material and fragility without being explicitly told, since misjudging this can crush or drop the object",
   "The robot must plan a stable grip in real time based on the object's 3D shape, which varies enormously across everyday items",
   "No physical robotic gripper has ever successfully picked up any object of any kind under laboratory conditions",
   "Force must be controlled precisely during the grasp, since too little grip drops the object and too much can damage it"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Estimating unfamiliar material/fragility, real-time 3D shape-based grasp planning, and precise force control are all genuine, well-documented components of why novel-object grasping remains hard. The claim that no gripper has ever picked up any object is simply false — grasping works well for known, familiar objects; it's specifically unfamiliar, irregular objects that remain challenging."
},
{
 "q": "Which of the following robots would most accurately be described as an AGV (Automated Guided Vehicle) rather than an AMR (Autonomous Mobile Robot)?",
 "options": [
   "A warehouse cart that follows a fixed magnetic strip embedded in the floor and stops completely if any object blocks that exact strip, without attempting to navigate around it",
   "A hospital delivery robot that builds its own map of the hallways and dynamically re-routes around an unexpected obstacle like a cart left in its usual path",
   "A search-and-rescue robot that explores an unknown, unmapped disaster site using its own onboard sensors to build a map as it goes",
   "A robot vacuum that uses SLAM to build a floorplan of a house it has never been inside before and plans its own cleaning route accordingly"
 ],
 "answer": 0,
 "explanation": "The defining feature of an AGV is following a fixed, predefined physical track or marking — cheap and reliable in controlled environments but brittle to any unexpected obstacle. The other three examples all involve building a map and planning routes independently, which is the defining feature of an AMR."
},
{
 "q": "A robotics startup wants their pick-and-place robot to successfully grasp fresh produce of wildly varying shapes without needing a specific pre-programmed grip strategy for every single fruit and vegetable. Which two design choices would most directly help with this specific challenge? Select all that apply.",
 "options": [
   "Using a soft, compliant gripper that can deform to match irregular shapes rather than a rigid, fixed-shape claw",
   "Investing in better real-time grasp-planning software that reasons about the object's geometry and stability from sensor data",
   "Reducing the robot's context window so it processes fewer sensor readings per second",
   "Painting all the produce a single uniform colour before it reaches the robot's picking station"
 ],
 "answer": [0, 1],
 "multi": True,
 "explanation": "A compliant gripper (soft robotics) and better real-time grasp planning are genuine, real approaches to handling irregular objects. 'Context window' is an LLM concept, not a robotics sensing concept, and repainting produce doesn't address the underlying shape-and-fragility problem the question is about."
},
{
 "q": "A university lab builds a rover intended for another planet, where a round-trip radio signal takes over 20 minutes, making real-time joystick control from Earth impossible. What robotics approach must the rover primarily rely on instead?",
 "options": [
   "A high degree of onboard autonomy — since real-time teleoperation is impossible over such a long communication delay, the rover must independently plan paths, avoid hazards, and make many decisions itself between the infrequent instructions it receives from Earth",
   "Pure teleoperation — mission controllers on Earth continue to control every single wheel movement of the rover in real time despite the twenty-minute communication delay, simply accepting the resulting lag",
   "Swarm robotics — the single rover coordinates with a large number of other simple identical rovers already present on the planet's surface to compensate for the communication delay",
   "SLAM is entirely unnecessary for this rover, since the planet's full surface map is already completely known in advance and does not need to be built or updated during the mission"
 ],
 "answer": 0,
 "explanation": "With a communication delay this long, true real-time teleoperation is physically impossible — by the time an operator sees a hazard and sends a correction, the rover could already have driven into it. Real planetary rovers rely on significant onboard autonomy for navigation and hazard avoidance between much sparser high-level instructions from mission control."
},
{
 "q": "A robotics engineer is deciding whether a new warehouse robot needs 6 degrees of freedom (like a human arm and wrist) or can manage with just 3, for a task that only involves picking items straight up and placing them straight down on a conveyor. What is the main tradeoff in choosing fewer degrees of freedom?",
 "options": [
   "Fewer degrees of freedom generally means a simpler, cheaper, and more reliable robot for a narrow task, but far less flexibility to handle any future task requiring more complex angles or orientations",
   "Degrees of freedom refers exclusively to how many separate robots are allowed to physically operate within the same shared workspace at any given moment in time",
   "Reducing degrees of freedom always improves the robot's grasping ability for irregular objects, since fewer moving joints means less mechanical complexity to precisely control during a grasp",
   "Degrees of freedom has no real engineering tradeoff at all, and a robot's cost and capability are determined entirely by its onboard software rather than its physical joint design"
 ],
 "answer": 0,
 "explanation": "Degrees of freedom describes the independent ways a robot's joints can move. Fewer degrees of freedom generally means simpler mechanics, lower cost, and higher reliability for a narrowly defined task, at the direct cost of flexibility if requirements later change to need more complex motion — a genuine, common engineering tradeoff in robot design."
},
{
 "q": "A precision-agriculture drone company advertises that their drones can identify individual plants under stress and apply fertiliser only to those specific plants, rather than spraying an entire field uniformly. What is the primary practical benefit of this approach over traditional uniform spraying?",
 "options": [
   "It reduces waste and cost by applying inputs like fertiliser only where and when actually needed, rather than uniformly over healthy and unhealthy areas alike",
   "It completely removes the need for the drone to have any onboard sensors, since identifying individual stressed plants can be done using GPS coordinates alone with no additional sensing required",
   "It guarantees a 100% crop yield increase in every field it is used on, regardless of soil quality, weather conditions, or any other variable affecting the farm",
   "It eliminates the need for any human farmer involvement whatsoever in decisions about the farm, since the drone becomes fully and permanently responsible for every agricultural decision"
 ],
 "answer": 0,
 "explanation": "Precision agriculture's core value proposition is targeted, plant-level application instead of blanket treatment — reducing waste and cost by treating only the areas that actually need it, based on real sensor data (imagery, moisture, stress indicators), not GPS coordinates alone."
},
{
 "q": "A da Vinci surgical robot lets a surgeon operate with tremor filtering and enhanced precision, while the surgeon remains fully in control of every movement decision throughout the operation. Which robotics concept does this best illustrate, and why is it used here rather than a fully autonomous surgical robot?",
 "options": [
   "Teleoperation — keeping a human directly in control for tasks requiring nuanced, high-stakes judgement, where full autonomy would remove essential human decision-making from a critical, safety-sensitive process",
   "Swarm robotics — the surgical robot is actually coordinating with several other simpler robots simultaneously in the operating room, even though only one robotic arm is visible to the surgeon and patient",
   "SLAM — the surgical robot is primarily focused on building a map of the operating room and tracking its own position within that room during the surgery, more than assisting the surgeon's hand movements",
   "Sim-to-real transfer — the robot was trained extensively on simulated surgeries beforehand and is now operating with zero human input at all during the real surgery, purely relying on that simulation training"
 ],
 "answer": 0,
 "explanation": "Surgical teleoperation deliberately keeps the surgeon's judgement and control central, with the robot providing precision and tremor filtering rather than making decisions itself — appropriate given how much nuanced, case-specific judgement real surgery requires, which is not yet something any robot can be trusted to fully automate."
},
{
 "q": "A robotics company is deciding whether their new home-assistant robot's face should be a simple, friendly cartoon display or a highly realistic synthetic human face. Based on established robotics design principles, which choice is generally safer for user comfort, and why?",
 "options": [
   "The cartoon design, because getting closer to full human realism without perfectly achieving it risks triggering the uncanny valley effect, whereas a design that is clearly non-human tends to avoid that discomfort",
   "The realistic human face, because research consistently shows that any humanoid robot becomes more comfortable to interact with the more perfectly human-like its appearance becomes, without exception",
   "Neither choice matters at all for user comfort, since the uncanny valley effect has only ever been observed in a laboratory setting and has never actually affected any real commercial product",
   "The realistic human face, because a synthetic human face is mechanically simpler and cheaper to manufacture at scale than a simplified cartoon-style robot display of equivalent durability"
 ],
 "answer": 0,
 "explanation": "The uncanny valley effect specifically predicts a dip in comfort as a robot's appearance approaches, but doesn't quite reach, full human realism — which is exactly why many commercially deployed social robots (like Pepper) deliberately choose clearly non-human, cartoonish designs rather than chasing photorealism."
},
{
 "q": "A robotics researcher wants to build a robot capable of exploring both a dry, dusty desert environment and a rocky, uneven cave system using the same hardware. Which of these is the most significant engineering challenge specific to this scenario, distinct from a robot designed for one predictable, flat environment?",
 "options": [
   "The robot's locomotion, sensing, and path planning must all be robust across two very different, unpredictable terrain types, rather than being optimised for just one known, consistent environment",
   "The robot no longer needs any onboard sensors at all, since a robot designed to operate in two different environments is defined specifically by having zero sensing capability of any kind",
   "The robot must be teleoperated at all times in both environments, since autonomous operation is technically impossible for any robot expected to handle more than a single terrain type",
   "The robot must use swarm robotics exclusively, since operating in two different environments is mathematically defined as requiring at least two or more physically separate robot units"
 ],
 "answer": 0,
 "explanation": "Designing for multiple unpredictable terrain types (rather than one controlled, known environment) genuinely raises the bar for locomotion robustness, sensing reliability, and path planning flexibility — a real, well-recognised challenge distinct from, and generally harder than, designing for a single predictable setting like a warehouse floor."
},
{
 "q": "A pick-and-place robot on a production line is described in its spec sheet as having 'high repeatability but a fixed, non-adaptive control program.' What does this combination most likely mean for how the robot would handle a small, unexpected change, like a box being placed slightly off its usual position?",
 "options": [
   "It would likely fail to adapt and either miss the box or place it incorrectly, since high repeatability means precisely repeating the same programmed motion, not adjusting to variation the program wasn't designed to handle",
   "It would automatically use SLAM and force-torque sensing to intelligently detect the box's actual position and adjust its motion accordingly, since these capabilities are guaranteed to exist in any repeatable robot",
   "It would seamlessly and correctly handle the change every time, since a robot's repeatability rating always directly measures its overall adaptability to unexpected changes in its environment",
   "It would immediately switch into teleoperation mode automatically, requesting a human operator to take manual control the moment any object in its environment appears in a slightly different position"
 ],
 "answer": 0,
 "explanation": "Repeatability specifically means a robot precisely repeats the same programmed motion every time — it says nothing about adaptability to variation. A robot with high repeatability but a fixed, non-adaptive program is exactly the kind of system that struggles with minor unexpected changes, unless it's specifically equipped with sensing and adaptive control it doesn't have here."
},
{
 "q": "Which of the following genuinely require solving a form of the sim-to-real gap, as the term is used in robotics? Select all that apply.",
 "options": [
   "A robot arm trained to grasp objects entirely in a physics simulator, later struggling to grasp the same objects reliably in the real world",
   "A walking robot trained in simulation performing a stable gait in that simulation, then falling over the first time it walks on a real, physical floor",
   "A robot's onboard camera producing a blurry image due to a loose lens that was never properly secured during manufacturing",
   "A drone's flight-control policy, tuned using a simplified aerodynamic simulator, behaving less precisely in real gusty outdoor wind conditions"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "The grasping, walking, and drone-flight examples are all genuine sim-to-real gap cases — a policy learned in an imperfect simulation failing to fully transfer to real-world physics. A loose camera lens is a hardware manufacturing defect, unrelated to the simulation-versus-reality gap the term specifically describes."
},
{
 "q": "A hospital is choosing between an AGV that follows a fixed magnetic floor strip and an AMR that builds its own map, for a robot that delivers medication between wards in a busy hospital where furniture and staff positions change throughout the day. Which is the better fit, and why?",
 "options": [
   "The AMR, because its ability to build its own map and adapt routes in real time handles the busy, frequently changing hospital environment far better than a fixed-track AGV that simply stops when its exact path is blocked",
   "The AGV, because a fixed magnetic floor strip is inherently more adaptable to daily changes in furniture and staff positions than any robot capable of building and updating its own map",
   "Neither option would work at all in a hospital environment, since medication-delivery robots are a purely theoretical concept that has never actually been deployed in any real hospital",
   "It makes no meaningful difference which one is chosen, since AGVs and AMRs are functionally identical technologies that differ only in their manufacturer's marketing terminology"
 ],
 "answer": 0,
 "explanation": "A dynamic, frequently changing environment like a busy hospital ward plays directly to an AMR's strength — building its own map and adapting routes in real time — whereas an AGV's fixed-track approach is a poor fit precisely because it can't route around the kind of everyday obstacles a hospital corridor regularly presents."
},
{
 "q": "A search-and-rescue team debates whether to send one large, expensive, highly capable robot or twenty small, cheap, simple robots into a partially collapsed building to search for survivors. What is the strongest argument in favour of the swarm of twenty simple robots?",
 "options": [
   "Multiple simple robots can search different areas in parallel and are individually expendable, so losing a few to structural collapse doesn't end the mission, unlike relying on a single expensive robot",
   "Twenty simple robots are always individually more intelligent than one large robot, since combining many robots automatically multiplies each individual robot's own onboard reasoning capability",
   "A swarm of twenty robots requires no path planning or coordination of any kind, since local rule-following automatically and perfectly avoids any need for the robots to plan routes at all",
   "Simple robots are immune to the sim-to-real gap entirely, meaning a policy that works in simulation is mathematically guaranteed to also work identically on all twenty real physical robots"
 ],
 "answer": 0,
 "explanation": "The core practical argument for swarm robotics in search-and-rescue is parallel coverage and resilience: many simple, individually expendable robots can search more ground simultaneously than one robot, and losing several to a hazard like further collapse doesn't end the mission — unlike a single point-of-failure expensive robot."
},
]
