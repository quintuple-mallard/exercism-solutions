function makeTally(teamData){
  let tally='Team                           | MP |  W |  D |  L |  P\n';
  let tallyRow=''
  for (const team of teamData){
    tallyRow=''
    tallyRow+=team['name'].padEnd(31,' ')+'|'+team['MP'].toString().padStart(3,' ')+' |'+team['W'].toString().padStart(3,' ')+' |'+team['D'].toString().padStart(3,' ')+' |'+team['L'].toString().padStart(3,' ')+' |'+team['P'].toString().padStart(3,' ')+'\n';
    tally+=tallyRow;
  }
  return tally;
}
function cleanData(games){//Transforms the string of games into an array of games, e.g. [[team1,team2,win]]
  let usefulGameData=[];
  games=games.split('\n');
  for (let idx=0;idx<games.length;idx++){
    usefulGameData.push(games[idx].split(';'))
  }
  return usefulGameData;
}
function getTeams(games){//takes output from cleanData and returns the teams
  let teams=[];
  for(const game of games){
    if (game==''){
      continue;
    }
    teams.push(game[0],game[1]);
  }
  return [...new Set(teams)];
}
export function tournamentTally(games){
  games=cleanData(games);
  let teams=getTeams(games);
  let teamStats=[];
  let statsPos={};
  for (const team of teams){
    teamStats.push({'name':team,'MP':0,'W':0,'D':0,'L':0,'P':0});
  }
  for (let idx=0;idx<teamStats.length;idx++){
    statsPos[teamStats[idx]['name']]=idx;
  }
  for (const game of games){
    if (game[2]==='draw'){
      teamStats[statsPos[game[0]]]['P']+=1;
      teamStats[statsPos[game[0]]]['MP']+=1;
      teamStats[statsPos[game[0]]]['D']+=1;
      teamStats[statsPos[game[1]]]['P']+=1;
      teamStats[statsPos[game[1]]]['MP']+=1;
      teamStats[statsPos[game[1]]]['D']+=1;
    }
    else if (game[2]==='win'){
      teamStats[statsPos[game[0]]]['P']+=3;
      teamStats[statsPos[game[0]]]['MP']+=1;
      teamStats[statsPos[game[0]]]['W']+=1;
      teamStats[statsPos[game[1]]]['MP']+=1;
      teamStats[statsPos[game[1]]]['L']+=1;
    }
    else if (game[2]==='loss'){
      teamStats[statsPos[game[1]]]['P']+=3;
      teamStats[statsPos[game[1]]]['MP']+=1;
      teamStats[statsPos[game[1]]]['W']+=1;
      teamStats[statsPos[game[0]]]['MP']+=1;
      teamStats[statsPos[game[0]]]['L']+=1;
    }
  }
  teamStats = sort(teamStats,'P','name');
  let fullTally=makeTally(teamStats);
  return fullTally.slice(0,-1);
}
function sort(data, pointsKey, nameKey) {
  return data.sort((a, b) => {
    const pointsComparison = b[pointsKey] - a[pointsKey]
    if (pointsComparison != 0) {
      return pointsComparison
    }
    return a[nameKey].localeCompare(b[nameKey])
  })
}