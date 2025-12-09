import { Tooltip, Button } from '@mantine/core';

export default function Home() {
  return (
    <div>
      <Tooltip label="Tooltip">
        <Button variant='filled' color='orange'>Button with tooltip</Button>
      </Tooltip>
    </div>
  );
}
