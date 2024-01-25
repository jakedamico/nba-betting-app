import React, { useState, useEffect } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/api/current-games")
      .then(result => result.json())
      .then(data => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <h1>NBA Games</h1>
      <Tabs>
        <TabList>
          <Tab>Tab 1</Tab>
          <Tab>Tab 2</Tab>
        </TabList>

        <TabPanel>
          <div>
            {data.length > 0 ? (
              data.map((game, index) => (
                <div key={index}>
                  <p>Game ID: {game.gameId}</p>
                  <p>
                    Teams: {game.awayTeam} at {game.homeTeam}
                  </p>
                  <p>Time: {new Date(game.gameTimeLTZ).toLocaleString()}</p>
                  <p>Status: {game.gameStatusText}</p>
                  {game.gameStatusText !== "Final" && (
                    <>
                      {game.gameClock && <p>Clock: {game.gameClock}</p>}
                      {game.quarter && <p>Quarter: {game.quarter}</p>}
                    </>
                  )}
                  <hr />
                </div>
              ))
            ) : (
              <p>Loading games...</p>
            )}
          </div>
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 2 */}
          <p>Content for Tab 2</p>
        </TabPanel>
      </Tabs>
    </div>
  );
}

export default App;
