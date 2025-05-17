import React from 'react';
import { useDropzone } from 'react-dropzone';
import { Snackbar } from '@mui/material';

export default function DropzoneUploader() {
  const [open, setOpen] = React.useState(false);
  const onDrop = (acceptedFiles) => {
    // Handle file upload
    setOpen(true);
  };
  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div>
      <div {...getRootProps()} style={{ border: '2px dashed #888', padding: '20px', textAlign: 'center' }}>
        <input {...getInputProps()} />
        <p>Przeciągnij tutaj plik CSV lub kliknij, aby wybrać</p>
      </div>
      <Snackbar
        open={open}
        autoHideDuration={3000}
        message="Plik załadowany"
        onClose={() => setOpen(false)}
      />
    </div>
  );
}
