# A Small Coaching Institute

## Overview
A teacher who used the previous application loved it and recommended it to a coaching institute. The coaching institute liked it too, but they have several students, teachers and classes. They want you to build a complete application for the institute.

## Details
### The structure
A coaching institute has several batches, and students are grouped into these batches based on their performance.    
The institute conducts weekly tests. Based on the students' marks, they're ranked. Based on their cumulative ranks, they rise or fall through batches.

### Administrator Interface
An administrator should see all batches and their students. This interface should have the following functions:

1. Upload a new marksheet with (student, marks).
2. Remap students to batches.

### Student Interface
A student can log in with his/her username/password. The interface he/she sees should show: 

1. His/her marks for the latest test.
2. His/her current batch.
3. *If you want to store a performance history, you can do so*.

### Further Details
1. All the interfaces are command line interfaces. Use stdout.
2. Use CSV/JSON. You can even try SQL (SQLite would be a good choice for this).
3. Keep the batch size small for testing. Maybe 2-3 students per batch, and 2-3 batches. 
4. Store the usernames, passwords in a file before executing the program. Currently, there are no features that help the user change/recover passwords. 
5. For remapping students to new batches, define a batch-strength and no-of-batches yourself and sort students by rank and distribute.
6. Assume that this program runs indefinitely
7. Simplicity is bliss.
