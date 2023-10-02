function returnName(){
    globalThis.playername = document.getElementById("userName").value;
    alert("player: " + playername);
}

function returnGuesses(){
    let guess_n = document.getElementById("userInput").value;
    alert("Guesses log for " + playername + ":\n" + dolog(guess_n))
}

log = ""
function dolog(guess){
    log = log + guess + "->" + getResult(guess) + "\n";
    return log
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

function myFilter(elm){
    return (elm != null);
}

first_num = getRandomInt(10).toString()
second_num = getRandomInt(10).toString()
third_num = getRandomInt(10).toString()
forth_num = getRandomInt(10).toString()
ans = first_num+second_num+third_num+forth_num

//document.write(first_num+second_num+third_num+forth_num)

function getResult(str)
{
  a = 0
  b = 0
  b_list = [0, 1, 2, 3]
  r_list = ['x', 'y', 'z', 'w']
  ans_list = [first_num, second_num, third_num, forth_num]
  for (step = 0; step < 4; step++)
    {
      
      if (Array.from(str)[step] == Array.from(ans)[step])
      {
       a += 1;
       b_list[step] = null;
      }
    }
  b_list = b_list.filter(myFilter)
  //document.write(b_list);
  for (const elem of b_list)
    {
      
      index = ans_list.indexOf(Array.from(str)[elem])
      if (index != -1)
        {
          b += 1;
          ans_list[index] = r_list[r_list.length - 1];
          r_list.pop();
        }
    }
  //document.write(ans_list);
  return a.toString()+"A"+b.toString()+"B"
}
