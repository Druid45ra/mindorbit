import React, { useState } from 'react';

export default function NoteEditor() {
  const [content, setContent] = useState('');

  return (
    <div className="p-4 bg-white rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Note Editor</h2>
      <textarea
        className="w-full border p-2 rounded"
        rows={6}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div className="mt-4">
        <h3 className="font-semibold">Preview:</h3>
        <pre className="bg-gray-100 p-2 rounded">{content}</pre>
      </div>
    </div>
  );
}
