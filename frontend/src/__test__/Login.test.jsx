import { render,screen } from '@testing-library/react';
import {Login} from '../Components/auth/Login'
import { expect } from 'vitest';

test('render login UI',()=>{
    render(<Login/>)
    expect(screen.getByRole('heading')).toHaveTextContent('Login')
})