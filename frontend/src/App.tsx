import React from 'react';
import NoteEditor from './components/NoteEditor';
import TaskList from './components/TaskList';
import HabitTracker from './components/HabitTracker';

function App() {
  return (
    <div className="min-h-screen p-8 grid grid-cols-1 md:grid-cols-3 gap-4 bg-gray-100">
      <NoteEditor />
      <TaskList />
      <HabitTracker />
    </div>
  );
}

export default App;
