const n = 200;
let doors = new Array(n).fill('close'); 

const toggleDoor = function(curState){
  return (curState === 'open') ? 'close' : 'open';
}

for(let i = 1; i <= n; i++) {
  doors = doors.map((state, idx) => {
    if((idx + 1) % i === 0){
      return toggleDoor(state);
    }

    return state;
  });
}

doors.forEach((state, idx) => {
  console.log(`door ${idx + 1}: ${state}`);
})