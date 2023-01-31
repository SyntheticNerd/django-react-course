import React from "react";
import { Card } from "react-bootstrap";

const Product = ({ product }) => {
  return (
    <Card className='my-3 py-3 rounded'>
      <a href={`/product/${product._id}`}>
        <Card.Img src={product.image} />
      </a>

      <Card.Body>
        <a href={`/product/${product._id}`}>
          <strong>{product.name}</strong>
        </a>
      </Card.Body>
    </Card>
  );
};

export default Product;
