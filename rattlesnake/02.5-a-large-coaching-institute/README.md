# A Large Coaching Institute

## Overview
A teacher who used the previous application loved it and recommended it to a coaching institute. The coaching institute liked it too, but they have several students, teachers and classes. They want you to build a complete application for the institute.

## Details
### The structure
A coaching institute has several batches, and students are grouped into these batches based on their performance.    
The institute conducts weekly tests. Based on the students' marks, they're ranked. Based on their cumulative ranks, they rise or fall through batches.
A batch has a unique teacher and a teacher has a unique batch.

### Administrator Interface
An administrator should be able to see all those teachers who have uploaded their mark lists and those who haven’t. This interface should have the following functions:

1. Remind teachers who haven’t submitted marklists.
2. Remap students to batches.
3. Start a new test (all the teachers now need to upload new mark lists).

2 and 3 can only happen if all teachers have submitted their previous mark lists.

### Student Interface
A student can log in with his/her username/password. The interface he/she sees should show: 

1. His/her marks for the latest test?
2. His/her current batch. 
3. *If you want to store a performance history, you can do so.*

### Teacher Interface
A teacher can log in with his/her username/password. A teacher should be able to: 

1. See the students in his/her batch.
2. Upload marks of each of the student of his/her batch in a file. This list will go to the administrator. If you don’t want to work with a file, you can do this manually, for example, the interface asks you, “How much did student 1 get?” 23 “How much did student 2 get?” 56 and so on. In any case, you’ll have to store a student - batch mapping of some sort.
3. The teacher should also be able to see in the interface if there’s a reminder from the administrator.

### Further Details
1. All the interfaces are command line interfaces. Use stdout.
2. Use CSV/JSON. You can even try SQL (SQLite would be a good choice for this).
3. Keep the batch size small for testing. Maybe 2-3 students per batch, and 2-3 batches. 
4. Store the usernames, passwords in a file before executing the program. Currently, there are no features that help the user change/recover passwords. Preferably keep the teacher/student username-password files separately.
5. Think up an approach to set the reminder for teachers. One naive approach would be to modify the value of a variable kept in the teacher’s file.
6. For remapping students to new batches, define a batch-strength and no-of-batches yourself and sort students by rank and distribute.
7. Assign teachers to student-batches manually, at the start.
8. Assume that this program runs indefinitely and keep it menu-driven, i.e, 
	
	* 1 - Remind Teachers, 
	* 2 - Remap Batches 
	* 3 - Set Reminder
	* 0 - Quit

9. In case you think this is too complex, worry not. We’ll release some skeleton code soon. 
10. Simplicity is bliss. [KISS Principle](https://en.wikipedia.org/wiki/KISS_principle)
