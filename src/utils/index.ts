import type { MessageFn } from 'element-plus'

interface Window {
  $message?: {
    error: MessageFn;
    success: MessageFn;
    warning: MessageFn;
    info: MessageFn;
  }
}

export const window = globalThis.window as Window