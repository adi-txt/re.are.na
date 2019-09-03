import React from "react"

import "../css/Block.css"

function Block(props) {
    return (
        <div id='media-block'>
          <a href={props.linksrc} target="_blank" rel="noopener noreferrer">
            <img
              src={props.imgsrc}
              alt='block'
            />
          </a>
        </div>
    )
}

export default Block
