import { useState } from "react";
export default function ConditionalComponent() {
  const [displayState, setDisplayState] = useState(false);
  
  //   if (displayState) {
  //     output = <h3>This conditional Component</h3>;
  //   } else {
  //     output = <h3>Nothing to see here</h3>;
  //   }
  return displayState ? (
    <h3>This conditional Component</h3>
  ) : (
    <h3>Nothing to see here</h3>
  );

  
}
