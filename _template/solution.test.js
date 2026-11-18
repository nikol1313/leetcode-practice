import { expect, test } from 'vitest';
import { solve } from './solution.js';

test.each([[[[1, 2, 3]], 0]])('solve(%j) -> %j', (args, expected) => {
  expect(solve(...args)).toEqual(expected);
});
