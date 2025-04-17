import React from 'react';

const MarkdownOutput = ({ markdown }) => {
    return (
        <div className="markdown-output">
            <h2>Extracted Requirements</h2>
            <div dangerouslySetInnerHTML={{ __html: markdown }} />
        </div>
    );
};

export default MarkdownOutput;