import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

export default function ChartCard({ title, children }) {
  return (
    <Card style={{ margin: '20px' }}>
      <CardContent>
        <Typography variant="h6">{title}</Typography>
        <div>{children}</div>
      </CardContent>
    </Card>
  );
}
