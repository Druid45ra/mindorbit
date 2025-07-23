import React, { useState } from 'react';

export default function HabitTracker() {
  const [completed, setCompleted] = useState(false);

  return (
    <div className="p-4 bg-white rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Habit Tracker</h2>
      <button
        className={`px-4 py-2 rounded ${completed ? 'bg-green-500' : 'bg-gray-300'}`}
        onClick={() => setCompleted(!completed)}
      >
        {completed ? 'Completed Today!' : 'Mark as Done'}
      </button>
    </div>
  );
}
