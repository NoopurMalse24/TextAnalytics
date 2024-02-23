// ImageGallery.js
import React, { useState } from 'react';
import './ImageGallery.css'; 

const ImageGallery = () => {
  const images = [
    "/images/img3.webp",
    "/images/img1.webp",
    "/images/img2.webp",
  ];

  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const handleLeftClick = () => {
    if (currentImageIndex > 0) {
      setCurrentImageIndex(prevIndex => prevIndex - 1);
    } else {
      setCurrentImageIndex(images.length - 1);
    }
  };

  const handleRightClick = () => {
    if (currentImageIndex < images.length - 1) {
      setCurrentImageIndex(prevIndex => prevIndex + 1);
    } else {
      setCurrentImageIndex(0);
    }
  };

  return (
    <div className="image-gallery">
      <img
        src={images[currentImageIndex]}
        alt={`Image ${currentImageIndex + 1}`}
        onClick={e => {
          const clickPosition = e.clientX - e.target.getBoundingClientRect().left;
          if (clickPosition < e.target.width / 2) {
            handleLeftClick();
          } else {
            handleRightClick();
          }
        }}
      />
    </div>
  );
};

export default ImageGallery;
